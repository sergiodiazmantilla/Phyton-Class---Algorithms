import cv2 
import csv 
import time 
import math 
import uuid 
import numpy as np 
from dataclasses import dataclass, field 
from collections import deque, defaultdict 
from typing import Dict, List, Tuple, Optional 
 
# ============================================================ 
# CONFIGURACION GENERAL 
# ============================================================ 
 
VIDEO_SOURCE = 0  # 0 para webcam, o ruta a video, o URL RTSP 
FRAME_WIDTH = 960 
FRAME_HEIGHT = 540 
 
# Umbrales generales 
MAX_MISSING_FRAMES = 30 
TRACK_DISTANCE_THRESHOLD = 80 
HISTORY_LENGTH = 30 
MIN_PERSON_DETECTION_WIDTH = 40 
MIN_PERSON_DETECTION_HEIGHT = 80 
 
# Umbrales de comportamiento 
LOITERING_SECONDS = 20               # permanencia alta 
REPETITIONS_THRESHOLD = 3            # veces entrando a zona sensible 
SPEED_HIGH_THRESHOLD = 180.0         # pixeles/segundo 
DIRECTION_CHANGE_THRESHOLD = 45.0    # grados para cambio brusco 
DOOR_INTERACTION_SECONDS = 6         # tiempo frente a puerta 
GROUP_DISTANCE_THRESHOLD = 120       # distancia para grupo 
AGGRESSIVE_SPEED_THRESHOLD = 220.0   # velocidad alta 
ABANDONMENT_SECONDS = 12             # objeto quieto mucho tiempo 
OBJECT_MIN_AREA = 900                # area minima para objeto abandonado 
 
# Horario inusual (ejemplo) 
UNUSUAL_HOURS = set(range(0, 6)) | set(range(23, 24)) 
 
# Archivo de registro 
EVENTS_CSV = "eventos_vigilancia.csv" 
 
# Mostrar trayectorias 
DRAW_TRAILS = True 
 
# ============================================================ 
# ZONAS DEL SISTEMA (editar segun tu escenario) 
 
# Cada zona: (x1, y1, x2, y2) 
# ============================================================ 
 
ZONES = { 
    "zona_sensible": (650, 120, 920, 480), 
    "zona_restringida": (760, 180, 930, 500), 
    "puerta": (700, 200, 790, 430), 
    "area_publica": (0, 0, 959, 539), 
} 
 
# ============================================================ 
# UTILIDADES 
# ============================================================ 
 
def current_timestamp() -> str: 
    return time.strftime("%Y-%m-%d %H:%M:%S") 
 
def point_in_rect(point: Tuple[int, int], rect: Tuple[int, int, int, 
int]) -> bool: 
    x, y = point 
    x1, y1, x2, y2 = rect 
    return x1 <= x <= x2 and y1 <= y <= y2 
 
def rect_center(rect: Tuple[int, int, int, int]) -> Tuple[int, int]: 
    x, y, w, h = rect 
    return (x + w // 2, y + h // 2) 
 
def euclidean(p1: Tuple[int, int], p2: Tuple[int, int]) -> float: 
    return float(math.hypot(p1[0] - p2[0], p1[1] - p2[1])) 
 
def angle_between(v1: Tuple[float, float], v2: Tuple[float, float]) -> float: 
    n1 = math.hypot(v1[0], v1[1]) 
    n2 = math.hypot(v2[0], v2[1]) 
    if n1 == 0 or n2 == 0: 
        return 0.0 
    dot = v1[0] * v2[0] + v1[1] * v2[1] 
    cosang = max(-1.0, min(1.0, dot / (n1 * n2))) 
    return math.degrees(math.acos(cosang)) 
 
def clamp(value: int, min_value: int, max_value: int) -> int: 
    return max(min_value, min(value, max_value)) 
 
def ensure_csv_header(path: str) -> None: 
    try: 
        with open(path, "x", newline="", encoding="utf-8") as f: 
            writer = csv.writer(f) 
            writer.writerow([ 
                "timestamp", "track_id", "risk_level", "alerts", 
                "tiempo_permanencia", "repeticiones_zona", "velocidad_movimiento", 
                "cambio_direccion", "entrada_zona_restringida", "objeto_abandonado", 
                "distancia_objeto_persona", "horario_inusual", "interaccion_puerta", 
                "movimiento_agresivo", "numero_personas_grupo", "cobertura_rostro" 
            ]) 
    except FileExistsError: 
        pass 
 
# ============================================================ 
# DATOS DE OBJETOS / PERSONAS 
# ============================================================ 
 
@dataclass 
class AlertState: 
    alerts: List[str] = field(default_factory=list) 
    risk_score: int = 0 
    risk_level: str = "BAJO" 
 
@dataclass 
class TrackedPerson: 
    track_id: str 
    bbox: Tuple[int, int, int, int] 
    centroid: Tuple[int, int] 
    first_seen: float 
    last_seen: float 
    missing_frames: int = 0 
 
    # Historial 
    trail: deque = field(default_factory=lambda:deque(maxlen=HISTORY_LENGTH)) 
    speed_history: deque = field(default_factory=lambda: deque(maxlen=HISTORY_LENGTH)) 
    direction_change_count: int = 0 
 
    # Variables medibles 
    tiempo_permanencia: float = 0.0 
    repeticiones_zona: int = 0 
    velocidad_movimiento: float = 0.0 
    cambio_direccion: int = 0 
    entrada_zona_restringida: int = 0 
    objeto_abandonado: int = 0 
    distancia_objeto_persona: float = -1.0 
    horario_inusual: int = 0 
    interaccion_puerta: int = 0 
 
    movimiento_agresivo: int = 0 
    numero_personas_grupo: int = 1 
    cobertura_rostro: int = 0  # Se deja en 0 por defecto; requeriria otro modelo 
 
    # Estados internos 
    zone_presence_started: Optional[float] = None 
    restricted_entered_prev: bool = False 
    sensitive_entered_prev: bool = False 
    door_presence_started: Optional[float] = None 
    last_zone_entry_time: float = 0.0 
    total_door_seconds: float = 0.0 
    aggressive_flag_frames: int = 0 
    last_logged_risk: str = "BAJO" 
 
    def update_bbox(self, bbox: Tuple[int, int, int, int], timestamp: float) -> None: 
        old_centroid = self.centroid 
        self.bbox = bbox 
        self.centroid = rect_center(bbox) 
        self.last_seen = timestamp 
        self.missing_frames = 0 
        self.trail.append((self.centroid, timestamp)) 
 
        # Calcular velocidad 
        if len(self.trail) >= 2: 
            prev_centroid, prev_ts = self.trail[-2] 
            dt = max(timestamp - prev_ts, 1e-6) 
            dist = euclidean(prev_centroid, self.centroid) 
            speed = dist / dt 
            self.velocidad_movimiento = speed 
            self.speed_history.append(speed) 
 
        # Calcular cambio de direccion 
        if len(self.trail) >= 3: 
            p1, _ = self.trail[-3] 
            p2, _ = self.trail[-2] 
            p3, _ = self.trail[-1] 
            v1 = (p2[0] - p1[0], p2[1] - p1[1]) 
            v2 = (p3[0] - p2[0], p3[1] - p2[1]) 
            ang = angle_between(v1, v2) 
            if ang >= DIRECTION_CHANGE_THRESHOLD: 
                self.direction_change_count += 1 
            self.cambio_direccion = self.direction_change_count 
 
    def mark_missing(self) -> None: 
        self.missing_frames += 1 
 
@dataclass  
class StationaryObject: 
    object_id: str 
    bbox: Tuple[int, int, int, int] 
    centroid: Tuple[int, int] 
    first_seen: float 
    last_seen: float 
    stationary_since: float 
    abandoned: bool = False 
 
# ============================================================ 
# DETECTOR DE PERSONAS 
# ============================================================ 
 
class PersonDetector: 
    def __init__(self) -> None: 
        self.hog = cv2.HOGDescriptor() 
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
 
    def detect(self, frame: np.ndarray) -> List[Tuple[int, int, int, int]]: 
        rects, weights = self.hog.detectMultiScale( 
            frame, 
            winStride=(6, 6), 
            padding=(8, 8), 
            scale=1.03 
        ) 
 
        detections = [] 
        for (x, y, w, h) in rects: 
            if w >= MIN_PERSON_DETECTION_WIDTH and h >= MIN_PERSON_DETECTION_HEIGHT: 
                detections.append((x, y, w, h)) 
        return self.non_max_suppression(detections, 0.35) 
 
    @staticmethod 
    def non_max_suppression(boxes: List[Tuple[int, int, int, int]], overlapThresh: float) -> List[Tuple[int, int, int, int]]: 
        if len(boxes) == 0: 
            return [] 
 
        boxes_np = np.array([[x, y, x + w, y + h] for x, y, w, h in boxes], dtype=np.float32) 
        pick = [] 
 
        x1 = boxes_np[:, 0] 
        y1 = boxes_np[:, 1] 
        x2 = boxes_np[:, 2] 
 
        y2 = boxes_np[:, 3] 
 
        area = (x2 - x1 + 1) * (y2 - y1 + 1) 
        idxs = np.argsort(y2) 
 
        while len(idxs) > 0: 
            last = len(idxs) - 1 
            i = idxs[last] 
            pick.append(i) 
 
            xx1 = np.maximum(x1[i], x1[idxs[:last]]) 
            yy1 = np.maximum(y1[i], y1[idxs[:last]]) 
            xx2 = np.minimum(x2[i], x2[idxs[:last]]) 
            yy2 = np.minimum(y2[i], y2[idxs[:last]]) 
 
            w = np.maximum(0, xx2 - xx1 + 1) 
            h = np.maximum(0, yy2 - yy1 + 1) 
            overlap = (w * h) / area[idxs[:last]] 
 
            idxs = np.delete( 
                idxs, 
                np.concatenate(([last], np.where(overlap > overlapThresh)[0])) 
            ) 
 
        result = [] 
        for i in pick: 
            x1i, y1i, x2i, y2i = boxes_np[i].astype(int) 
            result.append((x1i, y1i, x2i - x1i, y2i - y1i)) 
        return result 
 
# ============================================================ 
# TRACKER BASICO POR CENTROIDES 
# ============================================================ 
 
class CentroidTracker: 
    def __init__(self) -> None: 
        self.tracks: Dict[str, TrackedPerson] = {} 
 
    def update(self, detections: List[Tuple[int, int, int, int]], timestamp: float) -> Dict[str, TrackedPerson]:
        detection_centroids = [rect_center(det) for det in detections] 
 
        if len(self.tracks) == 0: 
            for det in detections: 
                track_id = str(uuid.uuid4())[:8] 
                person = TrackedPerson( 
                    track_id=track_id, 
 
                    bbox=det, 
                    centroid=rect_center(det), 
                    first_seen=timestamp, 
                    last_seen=timestamp 
                ) 
                person.trail.append((person.centroid, timestamp)) 
                self.tracks[track_id] = person 
            return self.tracks 
 
        unmatched_tracks = set(self.tracks.keys()) 
        unmatched_detections = set(range(len(detections))) 
        assignments: List[Tuple[str, int]] = [] 
 
        # Matriz de distancias 
        track_ids = list(self.tracks.keys()) 
        for track_id in track_ids: 
            if not unmatched_detections: 
                break 
 
            person = self.tracks[track_id] 
            best_det = None 
            best_dist = float("inf") 
 
            for det_idx in list(unmatched_detections): 
                dist = euclidean(person.centroid, detection_centroids[det_idx]) 
                if dist < best_dist and dist <= TRACK_DISTANCE_THRESHOLD: 
                    best_dist = dist 
                    best_det = det_idx 
 
            if best_det is not None: 
                assignments.append((track_id, best_det)) 
                unmatched_tracks.discard(track_id) 
                unmatched_detections.discard(best_det) 
 
        # Actualizar tracks emparejados 
        for track_id, det_idx in assignments: 
            self.tracks[track_id].update_bbox(detections[det_idx], timestamp) 
 
        # Marcar missing los no emparejados 
        for track_id in list(unmatched_tracks): 
            self.tracks[track_id].mark_missing() 
 
        # Crear tracks nuevos 
        for det_idx in unmatched_detections: 
            det = detections[det_idx] 
            track_id = str(uuid.uuid4())[:8] 
            person = TrackedPerson( 
                track_id=track_id, 
                bbox=det, 
                centroid=rect_center(det), 
                first_seen=timestamp, 
                last_seen=timestamp 
            ) 
            person.trail.append((person.centroid, timestamp)) 
            self.tracks[track_id] = person 
 
        # Eliminar tracks perdidos 
        for track_id in list(self.tracks.keys()): 
            if self.tracks[track_id].missing_frames > MAX_MISSING_FRAMES: 
                del self.tracks[track_id] 
 
        return self.tracks 
 
# ============================================================ 
# DETECCION HEURISTICA DE OBJETOS ABANDONADOS 
# ============================================================ 
 
class StationaryObjectDetector: 
    def __init__(self) -> None: 
        self.bg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True) 
        self.objects: Dict[str, StationaryObject] = {} 
 
    def update( 
        self, 
        frame: np.ndarray, 
        persons: Dict[str, TrackedPerson], 
        timestamp: float 
    ) -> Dict[str, StationaryObject]: 
        fg = self.bg.apply(frame) 
        _, fg = cv2.threshold(fg, 220, 255, cv2.THRESH_BINARY) 
        fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) 
        fg = cv2.dilate(fg, np.ones((5, 5), np.uint8), iterations=2) 
 
        contours, _ = cv2.findContours(fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
 
        person_boxes_xyxy = [] 
        for p in persons.values(): 
            x, y, w, h = p.bbox 
            person_boxes_xyxy.append((x, y, x + w, y + h)) 
 
        candidates = [] 
        for cnt in contours: 
 
            area = cv2.contourArea(cnt) 
            if area < OBJECT_MIN_AREA: 
                continue 
            x, y, w, h = cv2.boundingRect(cnt) 
            if h > 180 and w > 80: 
                # probablemente persona o gran region 
                continue 
 
            bbox_xyxy = (x, y, x + w, y + h) 
            overlaps_person = False 
            for px1, py1, px2, py2 in person_boxes_xyxy: 
                ix1 = max(x, px1) 
                iy1 = max(y, py1) 
                ix2 = min(x + w, px2) 
                iy2 = min(y + h, py2) 
                if ix2 > ix1 and iy2 > iy1: 
                    overlaps_person = True 
                    break 
 
            if not overlaps_person: 
                candidates.append((x, y, w, h)) 
 
        # emparejamiento simple 
        matched = set() 
        for obj_id, obj in list(self.objects.items()): 
            best_idx = None 
            best_dist = float("inf") 
            for i, det in enumerate(candidates): 
                if i in matched: 
                    continue 
                c = rect_center(det) 
                d = euclidean(c, obj.centroid) 
                if d < 50 and d < best_dist: 
                    best_dist = d 
                    best_idx = i 
            if best_idx is not None: 
                det = candidates[best_idx] 
                obj.bbox = det 
                obj.centroid = rect_center(det) 
                obj.last_seen = timestamp 
                if euclidean(obj.centroid, rect_center(det)) < 10: 
                    pass 
                matched.add(best_idx) 
 
        # crear nuevos 
        for i, det in enumerate(candidates): 
            if i in matched: 
                continue 
            obj_id = str(uuid.uuid4())[:8] 
 
            self.objects[obj_id] = StationaryObject( 
                object_id=obj_id, 
                bbox=det, 
                centroid=rect_center(det), 
                first_seen=timestamp, 
                last_seen=timestamp, 
                stationary_since=timestamp 
            ) 
 
        # depurar viejos 
        for obj_id in list(self.objects.keys()): 
            if timestamp - self.objects[obj_id].last_seen > 8: 
                del self.objects[obj_id] 
 
        # determinar abandono 
        for obj in self.objects.values(): 
            stationary_time = timestamp - obj.stationary_since 
            if stationary_time >= ABANDONMENT_SECONDS: 
                obj.abandoned = True 
 
        return self.objects 
 
# ============================================================ 
# ANALIZADOR DE COMPORTAMIENTO 
# ============================================================ 
 
class BehaviorAnalyzer: 
    def __init__(self) -> None: 
        self.last_event_log_time: Dict[str, float] = defaultdict(float) 
 
    def update_person_metrics( 
        self, 
        persons: Dict[str, TrackedPerson], 
        objects: Dict[str, StationaryObject], 
        timestamp: float 
    ) -> None: 
        person_ids = list(persons.keys()) 
 
        # Calcular grupos 
        for pid in person_ids: 
            p = persons[pid] 
            neighbors = 1 
            for pid2 in person_ids: 
                if pid == pid2: 
                    continue 
                p2 = persons[pid2] 
                if euclidean(p.centroid, p2.centroid) <= GROUP_DISTANCE_THRESHOLD: 
 
                    neighbors += 1 
            p.numero_personas_grupo = neighbors 
 
        for pid, p in persons.items(): 
            p.tiempo_permanencia = timestamp - p.first_seen 
            p.horario_inusual = 1 if time.localtime().tm_hour in UNUSUAL_HOURS else 0 
 
            # Zona sensible 
            in_sensitive = point_in_rect(p.centroid, ZONES["zona_sensible"]) 
            if in_sensitive and not p.sensitive_entered_prev: 
                if timestamp - p.last_zone_entry_time > 3: 
                    p.repeticiones_zona += 1 
                    p.last_zone_entry_time = timestamp 
            p.sensitive_entered_prev = in_sensitive 
 
            # Zona restringida 
            in_restricted = point_in_rect(p.centroid, ZONES["zona_restringida"]) 
            if in_restricted and not p.restricted_entered_prev: 
                p.entrada_zona_restringida = 1 
            p.restricted_entered_prev = in_restricted 
 
            # Puerta / interaccion 
            in_door = point_in_rect(p.centroid, ZONES["puerta"]) 
            if in_door: 
                if p.door_presence_started is None: 
                    p.door_presence_started = timestamp 
                p.total_door_seconds = timestamp - p.door_presence_started 
                if p.total_door_seconds >= DOOR_INTERACTION_SECONDS: 
                    p.interaccion_puerta = 1 
            else: 
                p.door_presence_started = None 
                p.total_door_seconds = 0.0 
 
            # Movimiento agresivo heuristico 
            if p.velocidad_movimiento >= AGGRESSIVE_SPEED_THRESHOLD and p.cambio_direccion >= 2: 
                p.aggressive_flag_frames += 1 
            else: 
                p.aggressive_flag_frames = max(0, p.aggressive_flag_frames - 1) 
 
            if p.aggressive_flag_frames >= 3: 
                p.movimiento_agresivo = 1 
 
            # Objeto abandonado cercano 
            p.objeto_abandonado = 0 
            p.distancia_objeto_persona = -1.0 
            min_dist = float("inf") 
            nearest_abandoned = None 
            for obj in objects.values(): 
                if obj.abandoned: 
                    d = euclidean(p.centroid, obj.centroid) 
                    if d < min_dist: 
                        min_dist = d 
                        nearest_abandoned = obj 
            if nearest_abandoned is not None: 
                p.distancia_objeto_persona = min_dist 
                if min_dist <= 140: 
                    p.objeto_abandonado = 1 
 
    def evaluate_risk(self, p: TrackedPerson) -> AlertState: 
        state = AlertState() 
 
        if p.tiempo_permanencia >= LOITERING_SECONDS: 
            state.risk_score += 2 
            state.alerts.append("Permanencia prolongada") 
 
        if p.repeticiones_zona >= REPETITIONS_THRESHOLD: 
            state.risk_score += 2 
            state.alerts.append("Merodeo en zona sensible") 
 
        if p.entrada_zona_restringida == 1: 
            state.risk_score += 5 
            state.alerts.append("Ingreso a zona restringida") 
 
        if p.interaccion_puerta == 1: 
            state.risk_score += 3 
            state.alerts.append("Interaccion prolongada con puerta/acceso") 
 
        if p.objeto_abandonado == 1: 
            state.risk_score += 4 
            state.alerts.append("Proximidad a objeto abandonado") 
 
        if p.horario_inusual == 1 and p.tiempo_permanencia > 10: 
            state.risk_score += 2 
            state.alerts.append("Actividad en horario inusual") 
 
        if p.movimiento_agresivo == 1: 
            state.risk_score += 5 
            state.alerts.append("Movimiento brusco/agresivo") 
 
        if p.numero_personas_grupo >= 3 and p.repeticiones_zona >= 2: 
            state.risk_score += 2 
 
            state.alerts.append("Comportamiento grupal coordinado") 
 
        if state.risk_score >= 8: 
            state.risk_level = "ALTO" 
        elif state.risk_score >= 4: 
            state.risk_level = "MEDIO" 
        else: 
            state.risk_level = "BAJO" 
 
        return state 
 
    def maybe_log_event(self, p: TrackedPerson, state: AlertState, now_ts: float) -> None: 
        # Loguear solo si es riesgo medio o alto y evitando spam 
        if state.risk_level == "BAJO": 
            return 
        if now_ts - self.last_event_log_time[p.track_id] < 8: 
            return 
 
        self.last_event_log_time[p.track_id] = now_ts 
 
        with open(EVENTS_CSV, "a", newline="", encoding="utf-8") as f: 
            writer = csv.writer(f) 
            writer.writerow([ 
                current_timestamp(), 
                p.track_id, 
                state.risk_level, 
                " | ".join(state.alerts), 
                round(p.tiempo_permanencia, 2), 
                p.repeticiones_zona, 
                round(p.velocidad_movimiento, 2), 
                p.cambio_direccion, 
                p.entrada_zona_restringida, 
                p.objeto_abandonado, 
                round(p.distancia_objeto_persona, 2) if p.distancia_objeto_persona >= 0 else -1, 
                p.horario_inusual, 
                p.interaccion_puerta, 
                p.movimiento_agresivo, 
                p.numero_personas_grupo, 
                p.cobertura_rostro 
            ]) 
 
# ============================================================ 
# DIBUJO Y VISUALIZACION 
# ============================================================ 
 
 
def draw_zone(frame: np.ndarray, rect: Tuple[int, int, int, int], label: str, color: Tuple[int, int, int]) -> None: 
    x1, y1, x2, y2 = rect 
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2) 
    cv2.putText(frame, label, (x1 + 4, y1 + 20), 
cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2) 
 
def draw_person(frame: np.ndarray, p: TrackedPerson, state: AlertState) -> None: 
    x, y, w, h = p.bbox 
    color = (0, 255, 0) 
    if state.risk_level == "MEDIO": 
        color = (0, 255, 255) 
    elif state.risk_level == "ALTO": 
        color = (0, 0, 255) 
 
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2) 
    cv2.circle(frame, p.centroid, 4, color, -1) 
 
    if DRAW_TRAILS and len(p.trail) > 1: 
        for i in range(1, len(p.trail)): 
            pt1 = p.trail[i - 1][0] 
            pt2 = p.trail[i][0] 
            cv2.line(frame, pt1, pt2, color, 2) 
 
    lines = [ 
        f"ID: {p.track_id}", 
        f"Riesgo: {state.risk_level} ({state.risk_score})", 
        f"Permanencia: {p.tiempo_permanencia:.1f}s", 
        f"Velocidad: {p.velocidad_movimiento:.1f}px/s", 
        f"Rep. zona: {p.repeticiones_zona}", 
        f"Camb. dir: {p.cambio_direccion}", 
        f"Restr.: {p.entrada_zona_restringida}", 
        f"Puerta: {p.interaccion_puerta}", 
        f"Agresivo: {p.movimiento_agresivo}", 
        f"Grupo: {p.numero_personas_grupo}", 
    ] 
 
    text_y = max(20, y - 10) 
    for i, line in enumerate(lines): 
        cv2.putText( 
            frame, line, 
            (x, text_y - i * 18), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1 
        ) 
 
    if state.alerts: 
        alert_text = " | ".join(state.alerts[:3]) 
        cv2.putText( 
 
            frame, alert_text, 
            (x, y + h + 18), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2 
        ) 
 
def draw_object(frame: np.ndarray, obj: StationaryObject) -> None: 
    x, y, w, h = obj.bbox 
    color = (255, 0, 0) if not obj.abandoned else (0, 0, 255) 
    label = "Objeto" if not obj.abandoned else "Objeto abandonado" 
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2) 
    cv2.putText(frame, label, (x, max(15, y - 5)), 
cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2) 
 
def draw_dashboard(frame: np.ndarray, persons: Dict[str, TrackedPerson], risks: Dict[str, AlertState], fps: float) -> None: 
    panel_h = 100 
    overlay = frame.copy() 
    cv2.rectangle(overlay, (0, 0), (frame.shape[1], panel_h), (30, 30, 30), -1) 
    frame[:] = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0) 
 
    total = len(persons) 
    altos = sum(1 for pid in risks if risks[pid].risk_level == "ALTO") 
    medios = sum(1 for pid in risks if risks[pid].risk_level == "MEDIO") 
 
    lines = [ 
        f"FPS: {fps:.1f}", 
        f"Personas detectadas: {total}", 
        f"Riesgo medio: {medios}", 
        f"Riesgo alto: {altos}", 
        f"Hora: {current_timestamp()}", 
        "Teclas: q=salir | s=guardar frame", 
    ] 
 
    for i, line in enumerate(lines): 
        cv2.putText(frame, line, (12, 24 + i * 16), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1) 
 
# ============================================================ 
# PROCESAMIENTO PRINCIPAL 
# ============================================================ 
 
def main() -> None: 
    ensure_csv_header(EVENTS_CSV) 
 
    cap = cv2.VideoCapture(VIDEO_SOURCE) 
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT) 
 
 
    if not cap.isOpened(): 
        raise RuntimeError("No se pudo abrir la fuente de video.") 
 
    detector = PersonDetector() 
    tracker = CentroidTracker() 
    object_detector = StationaryObjectDetector() 
    analyzer = BehaviorAnalyzer() 
 
    prev_time = time.time() 
 
    while True: 
        ok, frame = cap.read() 
        if not ok: 
            break 
 
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT)) 
        timestamp = time.time() 
 
        # Detectar personas 
        detections = detector.detect(frame) 
 
        # Actualizar tracker 
        persons = tracker.update(detections, timestamp) 
 
        # Detectar objetos estacionarios 
        objects = object_detector.update(frame, persons, timestamp) 
 
        # Analizar variables y riesgo 
        analyzer.update_person_metrics(persons, objects, timestamp) 
        risks: Dict[str, AlertState] = {} 
 
        for pid, person in persons.items(): 
            state = analyzer.evaluate_risk(person) 
            risks[pid] = state 
            analyzer.maybe_log_event(person, state, timestamp) 
 
        # Dibujar zonas 
        draw_zone(frame, ZONES["zona_sensible"], "Zona sensible", (0, 255, 255)) 
        draw_zone(frame, ZONES["zona_restringida"], "Zona restringida", (0, 0, 255)) 
        draw_zone(frame, ZONES["puerta"], "Puerta", (255, 255, 0)) 
 
        # Dibujar objetos 
        for obj in objects.values(): 
            draw_object(frame, obj) 
 
        # Dibujar personas 
 
        for pid, person in persons.items(): 
            draw_person(frame, person, risks[pid]) 
 
        # FPS 
        current = time.time() 
        fps = 1.0 / max(current - prev_time, 1e-6) 
        prev_time = current 
 
        # Dashboard 
        draw_dashboard(frame, persons, risks, fps) 
 
        cv2.imshow("Sistema de vigilancia inteligente", frame) 
 
        key = cv2.waitKey(1) & 0xFF 
        if key == ord("q"): 
            break 
        elif key == ord("s"): 
            fname = f"captura_{int(time.time())}.jpg" 
            cv2.imwrite(fname, frame) 
            print(f"Frame guardado: {fname}") 
 
    cap.release() 
    cv2.destroyAllWindows() 
 
if __name__ == "__main__": 
    main() 
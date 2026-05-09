import heapq
from dataclasses import dataclass, field

@dataclass(order=True)
class patiente:
    prioridad: int
    arrival_orde: int
    name: str = field(compare=False)
    diagnostico: str = field(compare=False)

class HospitalTiage:
    def __init__(self):
        self.heap = []
        self.Counter = 0
    def add_paciente(self, name, diagnostico, prioridad):
        
        # prioridad:
        # 1 = emergencia
        # 2 = urgencia
        # 3 = moderado
        # 4 = leve
        
        self.Counter +=1
        paciente = patiente(prioridad, self.Counter, name, diagnostico)
        heapq.heappush(self.heap, paciente)
    def atencion_next_paciente(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

def case_binario_tree_hospital():
    print("\n Arbol Binario Completo Aplicado al Triage Hospitalario")
    
    triage = HospitalTiage()
    triage.add_paciente("Ana","Dolor de Cabeza",4)
    triage.add_paciente("Luis","Accidente de trancito",1)
    triage.add_paciente("Rosa","Fiebre Alta",2)
    triage.add_paciente("Carlos","Dolor muscular",3)
    
    print("Orden de Atencion:")
    while True:
        paciente = triage.atencion_next_paciente()
        if paciente is None:
            break

        print(f"Atendiendo a {paciente.name} con diagnostico: {paciente.diagnostico} (Prioridad: {paciente.prioridad})")
case_binario_tree_hospital()
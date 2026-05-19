# Algoritmos Distribuidos
# Concepto
'''
Los algoritmos distribuidos resuelven problemas, 
colaborando entre múltiples nodos en una red.
Ejemplo en Python: Comunicación Cliente-Servidor
'''

# Explicacion
'''
Este ejemplo muestra la comunicación básica 
entre un servidor y un cliente usando sockets.
'''

import socket
import threading
#import time

def server():
    s = socket.socket()
    s.bind(('localhost', 5000))
    s.listen(1)
    #print("Servidor esperando conexión...")
    conn, _ = s.accept()
    #print("Cliente conectado:", addr)
    conn.send(b"Hola desde el servidor")
    conn.close()
    #s.close()
def client():
    #time.sleep(1)  # Espera a que el servidor inicie
    s = socket.socket()
    s.connect(('localhost', 5000))
    print(s.recv(1024).decode())
    s.close()

# Ejecutar servidor en paralelo
threading.Thread(target=server).start()
# Ejecutar cliente
client()
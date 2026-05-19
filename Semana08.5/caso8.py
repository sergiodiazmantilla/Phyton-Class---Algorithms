# Gestión de fallos en algoritmos distribuidos
# Concepto
'''
Ejemplo en Python: Retransmisión de Mensajes
'''

# Explicacion
'''
Este código simula el envío de mensajes 
con manejo básico de fallos.
'''

def send_message(node, message):
    try:
        print(f"Mensaje enviado a {node}: {message}")
    except Exception as e:
        print(f"Fallo al enviar a {node}: {e}")

nodes = ['A', 'B', 'C']
for node in nodes:
    send_message(node, "Actualización")
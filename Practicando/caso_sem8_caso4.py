import socket

server = socket.socket()

server.bind(("localhost", 5000))

server.listen(1)

print("Servidor web iniciado en http://localhost:5000")

conn, addr = server.accept()

# Leer petición del navegador
request = conn.recv(1024)

print(request.decode())

# Respuesta HTTP válida
response = """HTTP/1.1 200 OK

<h1>Hola desde Python Socket</h1>
"""

conn.send(response.encode())

conn.close()

server.close()
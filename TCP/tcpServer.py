import socket

ip = "127.0.0.1"
port = 12346

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(5)

print(f"Server running at {ip}:{port}")

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode("utf-8")
    client.send(data.upper().encode("utf-8"))
    client.close()
 
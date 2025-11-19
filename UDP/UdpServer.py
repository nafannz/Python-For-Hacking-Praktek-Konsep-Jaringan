import socket

ip = "127.0.0.1"
port = 12346

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

print(f"UDP server running at {ip}:{port}")

while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data.upper(), addr)

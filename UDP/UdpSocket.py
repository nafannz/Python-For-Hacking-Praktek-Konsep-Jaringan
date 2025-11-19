import socket

ip = "127.0.0.1"
port = 12346

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Message: ")
client.sendto(msg.encode("utf-8"), (ip, port))

data, _ = client.recvfrom(1024)
print("Reply:", data.decode("utf-8"))

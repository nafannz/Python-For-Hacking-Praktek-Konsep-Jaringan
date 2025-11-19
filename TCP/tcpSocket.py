import socket

ip = "127.0.0.1"
port = 12346

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

msg = input("Message: ")
client.send(msg.encode("utf-8"))

print("Reply:", client.recv(1024).decode("utf-8"))
client.close()
 
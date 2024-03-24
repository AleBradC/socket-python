import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("127.0.0.1", 7777))

socket.send(b"Salut") 
print(socket.recv(10).decode()) 

socket.close()

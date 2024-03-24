import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("0.0.0.0", 7777))
socket.listen(5)

cs, addr = socket.accept()
b = cs.recv(10)

print(b.decode()) 
cs.send(b"Hello")  
cs.close()

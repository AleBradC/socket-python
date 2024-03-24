import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg="hey"

socket.sendto(str.encode(msg),("127.0.0.1",7777))
msg,adr=socket.recvfrom(10)

print (msg.decode())
socket.close()
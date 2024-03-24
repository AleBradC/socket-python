import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("0.0.0.0", 7777))

# primesc & decodez
msg, adr = socket.recvfrom(10)
print(msg.decode())

message = "Salut"
socket.sendto(str.encode(message), adr) 
socket.close()

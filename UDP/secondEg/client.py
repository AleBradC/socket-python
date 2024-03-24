import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
firstNumber="4"
secondNumber="5"

socket.sendto(str.encode(firstNumber),("127.0.0.1",7777))
socket.sendto(str.encode(secondNumber),("127.0.0.1",7777))
serverMsg, serverAddress = socket.recvfrom(10)

print(serverMsg.decode())

socket.close()
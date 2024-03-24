import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("0.0.0.0", 7777))

firstNumber, clientAddress = socket.recvfrom(10)
secondNumber, clientAddress = socket.recvfrom(10)
print(firstNumber.decode())
print(secondNumber.decode())

serverMsg = firstNumber + secondNumber
socket.sendto(str.encode(serverMsg), clientAddress) 

socket.close()

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("0.0.0.0", 7777))

firstNumber, clientAddress = socket.recvfrom(10)
secondNumber, clientAddress = socket.recvfrom(10)
firstNumber = firstNumber.decode()
secondNumber = secondNumber.decode()

result = int(firstNumber) + int(secondNumber)
serverMsg = str(result).encode()

socket.sendto(serverMsg, clientAddress)

socket.close()

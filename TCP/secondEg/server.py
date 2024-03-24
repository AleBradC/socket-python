import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("0.0.0.0", 7777))
# maximum number of queued connections that the server can handle simultaneously
socket.listen(5)

# get from the client
socketConnection, addr = socket.accept()
clientMessage = socketConnection.recv(10)

print(clientMessage.decode()) 
print(addr[1])

# send to the client
address_sum = sum(int(digit) for digit in str(addr[1]))
socketConnection.send(str(address_sum).encode())

socketConnection.close()

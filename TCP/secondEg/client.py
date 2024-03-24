import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("127.0.0.1", 7777))

# get from console
for arg in sys.argv:
    arguments = arg

# send to the server
socket.send(str.encode(arguments)) 

# print what we get from the server 
print(socket.recv(10).decode()) 

socket.close()

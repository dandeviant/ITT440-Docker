#!/usr/bin/python3          # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect(("172.19.0.3", 12345))
receive = s.recv(1024)
print(receive.decode("utf-8"))
s.close()                     # Close the socket when done
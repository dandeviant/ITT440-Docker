#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from %s', addr)
   text = str("thank you for connecting")
   msg = bytes(text, "utf-8")
   c.send(msg)
   c.close()                # Close the connection

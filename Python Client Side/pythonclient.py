#!/usr/bin/python3
        #python shebang

import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect(("172.19.0.3", 12345))

print("\nRequesting Morbius latest points from server")
time.sleep(1)
receive = s.recv(1024)
print(receive.decode("utf-8"))
print("\n")
s.close()                     # Close the socket when done
exit()

#!/usr/bin/python3
	#python shebang

import socket               # Import socket module
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
host = "172.19.0.3"
port = 12345                # Reserve a port for your service.

s.connect(("172.19.0.3", 12345))
request = input("Enter user to find: ")
print("\nRequesting latest points of %s from server" %(request))
s.sendto(request.encode(), (host, port))
receive,addr = s.recvfrom(1024)
print("Points received from ", addr)
print("\n")
points = receive.decode("utf-8")

if points=="0":
  print("No record found for %s"%(request))
else:
  print("Points for %s: %s" %(request, points))
print("\n")


s.close()                     # Close the socket when done
exit()

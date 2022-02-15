#!/usr/bin/python3

import os
import socket
import time
try:
    import mysql.connector
    print('\nMySQL Connector installed')
except ImportError:
    print('\nMySQL Connector not installed')
    print('Installing for you')
    os.system('pip3 install mysql_connector_python')
    print("\n\n Restart the program")
    exit()

# Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

while True:
   data,addr = s.recvfrom(1024)
   print('Got connection from ', addr)
   request = data.decode()

   mydb = mysql.connector.connect(
    host="172.19.0.2",
    user="root",
    password="mysql",
    database="users"
   )

   print("Request: %s"%(request)) 
   cursor = mydb.cursor()
   sql = "SELECT points FROM user WHERE user='%s' "%(request)
   cursor.execute(sql)
   record = cursor.fetchall()
   print("Record: ", record)
   null = "[]"
   row = cursor.rowcount
   print("Number of row: %s"%(row))

   if row == 0:
     print(cursor.fetchall())
     print("No record found")
     msg = "0"
     s.sendto(bytes(msg.encode()), (addr[0], addr[1]))
   else:
     for x in record:
        record = cursor.fetchall()
        print("\nSelecting user ")

        print("=========================")
        print("Points    : ", x[0])
        print("=========================")
        print("Points: ", x[0])
        print("Addr: ", addr[0])
        print("Port: ", addr[1])
        print("")

        msg = str(x[0])
        s.sendto(bytes(msg.encode()), (addr[0], addr[1]))
        print("Points %s sent to client " %(msg))
        cursor.close()

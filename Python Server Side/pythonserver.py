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


# Connect to Database users in MySQL
mydb = mysql.connector.connect(
  host="172.19.0.2",
  user="root",
  password="mysql",
  database="users"
)

user = "Morbius"            # User for Python side is Morbius

# Create Socket
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen()                  # Listen to incoming connection
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from ', addr)
   mydb = mysql.connector.connect(
    host="172.19.0.2",
    user="root",
    password="mysql",
    database="users"
   )
   cursor = mydb.cursor()
   sql = "SELECT points FROM user WHERE user='%s' "% (user)
   cursor.execute(sql)
   result = cursor.fetchone()
   point = str(result[0])
   text = "[SERVER] Points for Morbius: %s" %(point)
   msg = bytes(text, "utf-8")
   c.send(msg)
   print("Morbius points : %s" %(point))   
   cursor.close()
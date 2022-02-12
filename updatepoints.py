#!/usr/bin/python3

import time
import os
try:
    import mysql.connector
    print('\nMySQL Connector installed')
except ImportError:
    print('\nMySQL Connector not installed')
    print('Installing for you')
    os.system('pip3 install mysql_connector_python')
    print("\n\n Restart the program")
    exit()

mydb = mysql.connector.connect(
  host="172.19.0.2",
  user="root",
  password="mysql",
  database="users"
)

#user is "Morbius" for Python side
user = "Morbius"
points = 0

def updates(points):
        time.sleep(2)
        point = str(points)
        print("Updated Points:", point)
        cont = 1 


try:
        cursor = mydb.cursor()
        sql = "SELECT points FROM user WHERE user='%s' "% (user)
        cursor.execute(sql)
        result = cursor.fetchone()
        cont = 1
        print("Default points : %s" %(result))
        points = result[0]              #Extract data from tuple
        while cont == 1:
                points += 1
                updates(points)

except KeyboardInterrupt:
        date = str(os.popen('date').read())
        datetime_stamp = date.strip()
        print("\nStopping Program\n");
        time.sleep(1)
        print("\nUpdating Points for Morbius")
        cursor = mydb.cursor()
        sql = "UPDATE user SET points = '%s', datetime_stamp =%s WHERE user='Morbius'; "
        value = (points, datetime_stamp)
        cursor.execute(sql, value)
        mydb.commit()
        print("Final Points Updated\n\n")
        exit()
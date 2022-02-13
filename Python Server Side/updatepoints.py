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
  host="172.19.0.4",
  user="root",
  password="mysql",
  database="users"
)

user = "Python Server"

try:
    mydb = mysql.connector.connect(
    host="172.19.0.4",
    user="root",
    password="mysql",
    database="users"
    )
    cont = 1
    cursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE origin_server='%s' "%(user)
    cursor.execute(sql)
    result = cursor.fetchall()
    while cont == 1:
        time.sleep(1)
        date = str(os.popen('date').read())
        datetime_stamp = date.strip()
        cursor = mydb.cursor()
        sql = "UPDATE user SET points=points+1, datetime_stamp ='%s' WHERE origin_server='Python Server'"%(datetime_stamp)
        cursor.execute(sql)
        mydb.commit()
        cursor.execute("SELECT user, points FROM user WHERE origin_server='Python Server' ")
        myresult = cursor.fetchall()
        print("Time of update: ", datetime_stamp)
        print("=========================")
        for x in myresult:
            print("User      : ", x[0])
            print("Points    : ", x[1])
            print("=========================")
        print("\n")
        cont = 1

except KeyboardInterrupt:
    date = str(os.popen('date').read())
    datetime_stamp = date.strip()
    print("\nStopping Program\n");
    time.sleep(1)
    print("Final Points Updated\n\n")
    exit()
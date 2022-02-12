#!/usr/bin/python3
import os

try:
    import mysql.connector
    print('\nMySQL Connector installed')
except ImportError:
    print('\nMySQL Connector not installed')
    print('Installing for you')
    os.system('pip3 install mysql_connector_python')
    # os.popen("zenity --warning --text='Installing MySQL'");
    print("\n\n Restart the program")
    exit()

mydb = mysql.connector.connect(
  host="172.19.0.2",
  user="root",
  password="mysql",
  database="users"
)

def view():
	print("\n=========================\n")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM user")
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)
	print("\n=========================\n")

def insert():
	mycursor = mydb.cursor()
	user = input("Enter User Name: ")
	points = input("Enter number of points: ")
	date = str(os.popen('date').read())
	datetime_stamp = date.strip()
	sql = "INSERT INTO user (user, points, datetime_stamp) VALUES (%s, %s, %s)"
	value = (user, points, datetime_stamp)
	mycursor.execute(sql, value)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	cont=1

cont = 1
while cont == 1:
	print("Select Options")
	print("\n [1]     View All")
	print(" [2]     Insert")
	print(" [Other] Leave")
	choice = input("\nEnter Choice: ")
	if choice=="1":
		view()
		cont=1
	elif choice=="2":
		insert()
		cont=1
	else:
		cont=0
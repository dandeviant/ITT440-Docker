#!/usr/bin/python3
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

def view():
	print("\n=========================")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM user")
	myresult = mycursor.fetchall()
	for x in myresult:
		print("User      : ", x[0])
		print("Points    : ", x[1])
		print("Timestamp : ", x[2])
		print("Added from: ", x[3])
		print("=========================")

def insert():
	mycursor = mydb.cursor()
	user = input("Enter User Name: ")
	points = input("Enter number of points: ")
	date = str(os.popen('date').read())
	datetime_stamp = date.strip()
	origin_server = "Python Server"
	sql = "INSERT INTO user (user, points, datetime_stamp, origin_server) VALUES (%s, %s, %s, %s)"
	value = (user, points, datetime_stamp, origin_server)
	mycursor.execute(sql, value)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	cont=1

def replace():
        mycursor = mydb.cursor()
        olduser = input("Enter user to be replaced: ")
        print("Replaced User: %s"%(olduser))
        sql = "SELECT * FROM user WHERE user='%s'"%(olduser)
        print("Query: %s"%(sql))
        mycursor.execute(sql)
        record = mycursor.fetchall()
        row = mycursor.rowcount
        if row == 0:
            print("\nERROR: User Not Found. Back to main.")
        else:
            newuser = input("\nEnter New User Name: ")
            points = input("Enter New number of points: ")
            date = str(os.popen('date').read())
            datetime_stamp = date.strip()
            origin_server = "Python Server"
            sql = "UPDATE user SET user='%s', points='%s', datetime_stamp='%s', origin_server='%s' WHERE user='%s'"%(newuser, points, datetime_stamp, origin_server, olduser)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record updated\n\n")
            cont=1



cont = 1
while cont == 1:
        mydb = mysql.connector.connect(
              host="172.19.0.2",
              user="root",
              password="mysql",
              database="users"
        )
        print("Select Options")
        print("\n [1]     View All")
        print(" [2]     Insert")
        print(" [3]     Replace")
        print(" [Other] Leave")
        choice = input("\nEnter Choice: ")
        if choice=="1":
                view()
                cont=1
        elif choice=="2":
                insert()
                cont=1
        elif choice=="3":
                replace()
                cont=1
        else:
                cont=0

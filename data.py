import mysql.connector	
from mysql.connector import Error
import pandas as pd
import getpass
import os

dbms = mysql.connector.connect(host= 'localhost', user= 'root', passwd= 'root', database= 'credentials') #If you are copying this so remember to put in your SQL host, user and password

curs = dbms.cursor() #point at operators in mysql


def menu():
	os.system('cls')
	print('''		
		                  
			1) log in		
			2) sign up		
			3) help		    
			4) exit			
							
		''')
	opt = int(input("enter your choice in digits: "))
	if opt == 1:
		login()
	elif opt == 2:
		signup()
	elif opt == 3:
		help()
	elif opt == 4:
		exit()
	else:
		print("Why are you joking?")

#startup UI


def userid():
	os.system('cls')
	ii = input("enter your User ID: ")
	curs.execute("SELECT ID FROM users")  #shows ID row of users table
	rows = curs.fetchall()  #fetch all data of ID row

	if (ii,) in rows:  #if value of ii is in the row, condition evaluates
		password()
	else:
		exit()


def password():
	ps = getpass.getpass("enter your pin: ")
	curs.execute("SELECT pin FROM users")    #shows PIN row of users table
	row = curs.fetchall()   #fetch all data of pin row

	if (ps,) in row:    #if data in row matches with data in ps, condition evaluates
		main()
	else:
		exit()


def login():
	userid()


def exit():
	os.system('cls')
	print("I think, you need time. Bye!")
	input("press enter...")


def signup():
	os.system('cls')
	nme = input("enter your name: ")
	usid = input("enter your userID: ")
	curs.execute("SELECT ID FROM users")
	rows = curs.fetchall()

	if (usid,) in rows:
		print("This userID is already taken. please select a different one.")
		signup()
	else:
		pasd = getpass.getpass("please enter a pin in digits, characters are not supported: ")
		entry = """insert into users (name, ID, pin) values(%s, %s, %s)"""
		data = (nme, usid, pasd)
		curs.execute(entry, data)
		dbms.commit()
		menu()


def main():
	os.system('cls')
	print("programme successful!!")


def help():
	os.system('cls')
	print('''If you are already an user, enter 1 and in the next window,
	enter your credentials.
	If you are a new user, enter 2 and hit enter and in the next window, do as directed.''')
	input('press enter to go back...')
	menu()
	

menu()


import random
import time
import os
from tqdm import tqdm
import random
import getpass

def loading():
	for index in tqdm(range(100), desc = "loading..."):
		time.sleep(0.1)

	pss = random.randint(1, 9)
	print("found a digit-", pss)
	print("hunt will continue in 2 seconds...")

def pas():
	pas = getpass.getpass("enter password: ")
	if pas == ("vanquisher"):
		menu()
	else:
		end()

def login():
	usid = input("enter username: ")
	if usid == ("vanquisher"):
		pas()
	else:
		end()

def end():
	os.system('cls')
	print("okk!! bye...")
	exit()


def menu():
	os.system('cls')
	input("enter ip address:")
	os.system('cls')
	print("starting the hunt...")
	time.sleep(2)
	os.system('cls')

	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	time.sleep(2)
	loading()
	print("completed! combine the digits and that's your password...")
	end()

login()

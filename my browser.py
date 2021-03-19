import webbrowser
import time

def srch():
	src = input("search anything--")
	print("search will begin soon.")
	time.sleep(2)
	webbrowser.open('https://duckduckgo.com/?t=ffab&q='+str(src))
	exit()
def url():
	srchh = input("enter URL--")
	webbrowser.open(srchh)
	print("search will began shortly")
	time.sleep(2)
	exit()

print('''to browse freely enter 1
to browse with url enter 2''')
what = int(input())

if what == 1:
	srch()
elif what == 2:
	url()
else:
	print("are you comedy me!!")
	exit()

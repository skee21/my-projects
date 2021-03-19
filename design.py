import turtle

forw = 10

tut = turtle.Turtle()
tut.speed(1000)
turtle.bgcolor('yellow')

while True:
	tut.forward(forw)
	tut.left(150)
	tut.left(10)
	forw += 2

turtle.done()
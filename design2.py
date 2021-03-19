import turtle

colors = ['green','black','green','black','green','black']

t = turtle.Pen()
turtle.bgcolor('black')

for i in range(500):
	t.pencolor(colors[i%6])
	t.width(i/100+1)
	t.forward(i)
	t.left(80)

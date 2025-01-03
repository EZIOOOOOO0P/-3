import turtle 
from turtle import *
 
wn = Screen( )
wn.bgcolor('skyblue')

t = turtle.Turtle( )
t.pencolor('black')

def curve( ):
	for i in range(200):
		t.rt(1)
		t.fd(1)

def heart( ):
	t.fillcolor('red')
	t.begin_fill( )
	t.lt(140)
	t.fd(113)
	curve( )
	t.lt(120)
	curve( )
	t.fd(122)
	t.end_fill( )
	
heart( )
t.ht( )

def write(message,pos):
	x,y=pos
	t.penup( )
	t.goto(x,y)
	t.color('blue')
	style=('stencil Std', 5, 'italic')
	t.write(message,font=style)
	
write('UR' ,(-68,95))
write('PRETTY' ,(-30,95))
wn.mainloop( )
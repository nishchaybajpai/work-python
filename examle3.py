from turtle import *

pencolor('black')
pensize(3)
fillcolor('blue')
speed('fastest')
for i in range(10,2,-1):
    begin_fill()
    circle(i*100)
    rt(250)
    end_fill()
goto(20,250)
mainloop()
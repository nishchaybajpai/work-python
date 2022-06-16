from turtle import *
import random
s = Screen()
s.setup(50,50)
colors = ['pink','orange']
speed('fastest')
for i in range(50):
    x = random.randint(-20,20)
    y = random.randint(-20,20)
    penup()
    goto(x,y)
    pendown()
    #write(f'{x},{y}')
    pensize(random.randint(1,2))
    pencolor(colors[random.randint(0,1)])
    radius = random.randint(5,30)
    fillcolor('black')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
mainloop()

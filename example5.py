from turtle import *
s = Screen()
s.setup(1000,700)
Colors = ['purple','blue']
pencolor('green')
pensize(5)
for i in range(6,0,-1):
    penup()
    setpos(0,2*i)
    pendown()
    fillcolor(Colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()
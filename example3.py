from turtle import *

t = Turtle()
t.speed('slowest')
s = getscreen()
for i in range(100):
    t.fd(100)
    t.lt(360//8)
    t.dot(20)
    t.circle(50,180)

    
mainloop()
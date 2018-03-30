import turtle 

t = turtle.Turtle()

t.speed(0)

cl = ['red', 'green', 'blue']

def drawArt(d, angle,x,y):
    c = 0
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(1,100):
        t.pencolor(cl[c])
        t.forward(d)
        t.left(angle)
        d = d-1
        c = c + 1
        if(c>2):
            c = 0
for i in range(20):
    drawArt(150,98,78,50)



import turtle

colors=["red" , "blue" , "white" , "yellow"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length=10

while length<500:
    t.forward(length)
    t.pencolor(colors[length%4])
    t.right(89)
    length +=5

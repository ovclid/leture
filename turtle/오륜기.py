import turtle
t=turtle.Turtle()
t.shape("turtle")

a = 100
t.width(10)

t.color("yellow")
t.up()
t.goto(0,100)
t.down()
t.circle(a)

t.color("green")
t.up()
t.goto(200,100)
t.down()
t.circle(a)

t.color("blue")
t.up()
t.goto(-50,200)
t.down()
t.circle(a)

t.color("black")
t.up()
t.goto(100,200)
t.down()
t.circle(a)

t.color("red")
t.up()
t.goto(250,200)
t.down()
t.circle(a)


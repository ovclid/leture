import turtle

def gotoandprint(x, y):
    print( f"({x},{y})" )

    """
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    return gotoresult
    """

def moveto(nation):
    t.up()
    t.goto(pos_dic[nation])
    t.down()
    
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("pink")
screen.bgpic("world_map.gif")
screen.onscreenclick(gotoandprint)

pos_dic = {"한국" : (-80.0, 53.0),
               "미국" : (439.0,47.0),
               "중국" : (-181.0,47.0) ,
               "호주" : (-52.0, -168.0),
               "러시아" : (-164.0,180.0),
               "캐나다" : (358.0,137.0),
               }


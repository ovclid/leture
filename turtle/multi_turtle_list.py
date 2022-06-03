#%%
import turtle
import time
t_list = []
each_dir_tnum = 2

screen = turtle.Screen()
#screen.setup(width=1600, height=1600)
screen.bgcolor("pink")
screen.bgpic("world_map.gif")


# 각 섹터별 터틀 생성
for i  in range(4):
    sub_list = []
    for j in range(each_dir_tnum):
        t = turtle.Turtle(shape="turtle")
        sub_list.append(t)
    t_list.append(sub_list)


# 각 섹터별 터틀 방향 전환 및 전방으로 이동
for i in range(4):
    for j in range(each_dir_tnum):
        #t_list[i][j].left(i*90)
        t_list[i][j].setheading(i*90)
        t_list[i][j].forward( (j+1) * 100)

 

# 각 섹터별 터틀 대각선 방향(좌향 135도) 전환 및 직사각형 빗면 만큼 이동
for i in range(4):
	for j in range(each_dir_tnum):
		t_list[i][j].left(135)
		t_list[i][j].forward((2** (1/2)) * (j+1) * 100)



turtle.exitonclick()
# %%
turtle.exitonclick()

# %%

#%%
import turtle

t_list = []
t_pos = []

sector = 4
each_dir_tnum = 3

screen = turtle.Screen()
#screen.setup(width=1600, height=1600)
screen.bgcolor("pink")
screen.bgpic("world_map.gif")

# 각 섹터별 터틀 생성
for i  in range(sector):
    sub_list = []
    
    for j in range(each_dir_tnum):
        t = turtle.Turtle(shape="turtle")
        sub_list.append(t)
        
    t_list.append(sub_list)

# 각 섹터별 터틀 방향 전환 및 전방으로 이동
for i in range(sector):
    sub_pos = []
    for j in range(each_dir_tnum):
        t_list[i][j].setheading(i*360/sector)
        t_list[i][j].forward( (j+1) * 100)

        sub_pos.append(t_list[i][j].pos())
    t_pos.append(sub_pos)
    
# 각 섹터별 터틀을 다른 섹터의 위치로 이동
for i in range(sector):
        for j in range(each_dir_tnum):
                if i == sector -1 :  # 마지막 섹터는 첫 섹터의 위치로 이동
                    t_list[i][j].goto(t_pos[0][j])
                else:
                    t_list[i][j].goto(t_pos[i+1][j])

turtle.exitonclick()

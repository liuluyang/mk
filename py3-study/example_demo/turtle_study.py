
import turtle
from turtle import *
import time

"""
五环
"""
############################################# 准备工作
turtle.screensize(200, 200)  # 控制画板大小
turtle.pensize(1)            # 控制画笔的粗细
turtle.speed(1)              # 控制速度

# turtle.hideturtle()        # 可以隐藏画笔


############################################ 画图

# turtle.color('blue')
# turtle.fd(-100)
# turtle.seth(90)
# turtle.circle(-50, 180)

turtle.color('blue')      # 设置画笔颜色
turtle.circle(80)         # 画圆
#
turtle.penup()            # 抬笔
turtle.forward(100)       # 平行移动
turtle.pendown()           # 落笔

turtle.color('black')
turtle.circle(80)

turtle.goto(-80, 80)


#
# turtle.penup()
# turtle.forward(180)
# turtle.pendown()
# turtle.color('red')
# turtle.circle(80)

# turtle.goto(-80, 80)
#
# turtle.penup()
# #turtle.forward(-400)
# turtle.goto(90, -80)
# turtle.pendown()
# turtle.color('yellow')
# turtle.circle(80)
#
# turtle.penup()
# #turtle.forward(-400)
# turtle.goto(270, -80)
# turtle.pendown()
# turtle.color('green')
# turtle.circle(80)

# turtle.forward(50)
# for i in range(10):
#     turtle.circle(i*5)
#     turtle.penup()
#     turtle.goto(0, -i*5)
#     turtle.pendown()


# turtle.fillcolor('red')
# turtle.begin_fill()
# turtle.circle(10)
# for _ in range(5):
#     turtle.forward(200)
#     turtle.right(144)
#     #turtle.left(111)
# turtle.end_fill()



turtle.done()

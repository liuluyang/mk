import turtle
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


turtle.color('blue')      # 设置画笔颜色
turtle.circle(80)         # 画圆

turtle.penup()            # 抬笔
turtle.forward(100)       # 平行移动
turtle.pendown()           # 落笔

turtle.color('black')
turtle.circle(80)

turtle.goto(-80, 80)





###############################################

turtle.done()
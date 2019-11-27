

import turtle
import random
import time

"""
五环
"""
############################################# 准备工作
turtle.screensize(1200, 1200)  # 控制画板大小
turtle.pensize(1)            # 控制画笔的粗细
turtle.speed(10)              # 控制速度

turtle.hideturtle()        # 可以隐藏画笔


############################################ 画图

# turtle.color('blue')
# turtle.fd(-100)
# turtle.seth(90)
# turtle.circle(-50, 180)

# turtle.color('blue')      # 设置画笔颜色
# turtle.circle(80)         # 画圆
# #
# turtle.penup()            # 抬笔
# turtle.forward(100)       # 平行移动
# turtle.pendown()           # 落笔
#
# turtle.color('black')
# turtle.circle(80)


"""
随机线条
"""
# color_list = ['blue', 'black', 'green', 'red', 'orange', 'white', 'yellow']
# for i in range(100):
#
#     turtle.color(random.choice(color_list))
#     turtle.goto(random.randrange(-1000, 1001), random.randrange(-1000, 1001))
#     time.sleep(0.01)


"""
画个五角星
"""

# base_width = 100
# position = [
#             [base_width*5, 0], [base_width, -base_width*3.5],
#             [base_width*2.5, base_width*2], [base_width*4, -base_width*3.5],
#             [0, 0]
#             ]
# turtle.color('blue')
# for p in position:
#     turtle.goto(*p)
#     # time.sleep(0.5)


"""
画多边形
"""
# turtle.write('hello world')  # 写入文字
# turtle.bgcolor('black')
# nums = int(input('想画几边形：'))
# point = 360 // nums
# for i in range(500):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.pencolor(r, g, b)
#     turtle.forward(50 + i)
#     turtle.right(point + 1)


"""
画圆圈
"""
# turtle.bgcolor('black')
# num = 0.1
# for i in range(500):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.pencolor(r, g, b)
#     turtle.forward(num)
#     turtle.right(-10)
#     num += 0.1


turtle.done()

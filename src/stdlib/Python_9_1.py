import turtle as t
from math import *

# turtle库概述
# 1.引用turtle库方式
'''
第一种，import turtle，则对turtle库中函数调
用采用turtle.<函数名>()形式。

第二种，from turtle import *
，则对turtle库中
函数调用直接采用<函数名>()形式，不在使用
turtle.作为前导。

第三种，import turtle as t，则对turtle库中函数
调用采用更简洁的t.<函数名>()形式，保留字as
的作用是将turtle库给予别名t。
'''
# t.circle(200)
# 2、turtle库包含100多个功能函数，主要包括窗体函数、画笔状态函数、画笔运动函数等三类。
# 2.1、窗体函数
'''
turtle.setup(width, height, startx, starty)
窗体函数
作用：设置主窗体的大小和位置
参数：
width ：窗口宽度，如果值是整数，表示的像素值；如果值
是小数，表示窗口宽度与屏幕的比例；
height: 窗口高度，如果值是整数，表示的像素值；如果
值是小数，表示窗口高度与屏幕的比例；
startx：窗口左侧与屏幕左侧的像素距离，如果值是None
，窗口位于屏幕水平中央；
starty：窗口顶部与屏幕顶部的像素距离，如果值是None
，窗口位于屏幕垂直中央；
'''
t.setup(600, 500, None, None)
# 设置画布长600，宽500，居中
# 设置六边形为半径30的圆内切六边形
for y in range(11):
    pen_y = 190 - 45 * y
    pen_x = -300 - 7.5 * sqrt(3) * pow(-1, y) + 7.5 * sqrt(3)
    t.penup()
    t.goto(pen_x, pen_y)
    t.pendown()
    for x in range(12):
        t.circle(30, steps=6)
        t.penup()
        t.forward(30 * sqrt(3))
        t.pendown()
t.done()

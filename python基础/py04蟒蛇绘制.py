#PythonDraw.py
'''
(1)canvas画布
设置画布大小：
turtle.screensize(canvwidth=None,canvheigh=None,bg=None)
整数：像素，小数：屏占比
(2)turtle海龟
import turtle #引入turtle绘图库
turtle的方法
turtle.setup(width,height,startx,starty) #绘图窗体
#海龟默认向右
turtle.fd(d) #向前走d距离
turtle.bk(d) #向后走d距离
turtle.circle(r,angle) #圆心默认在左侧，向左画圆
seth(angle) #改变前进方向，角度可以为负数
turtle.left(angle) #旋转
turtle.right(angle)
turtle.pensize()
turtle.pencolor()
turtle.speed(speed) #范围[0,10]整数


'''
import turtle
turtle.setup(650.35,200,200)
turtle.penup()
#抬起
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range (4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
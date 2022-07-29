# PythonDraw-Practice4

import turtle as t
import math

L = 150
p = math.pi / 180
t.penup()
t.seth(90)
t.fd(L)
t.pendown()
t.seth(0)
for i in range(1, 9):
    if i % 2 == 1:
        t.pendown()
        t.circle(-L, 45)
        t.right(90)
        t.fd(300)
        t.fd(-300)
        t.left(90)
    if i % 2 == 0:
        t.penup()
        t.circle(-L, 45)
        t.pendown()
        t.right(90)
        t.fd(300)
        t.fd(-300)
        t.left(90)
    # for循环到这里就结束了，但要注意，这里最后等于8，因此，画笔是抬起来的。
# 这时,pen在(0,150),且画笔抬起状态
t.done()

# 【参考代码】
# WindWheel.py
import turtle as t

t.pensize(2)
for i in range(4):  # 分为四个部分来画，将四片叶片分开绘制
    t.seth(90 * i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    # 画完弧形之后可以不用变换角度，因为goto函数不在意当时是什么角度，就能将两点连接起来。
    t.goto(0, 0)  # 画着回到原点

### 对于circle函数，即circle(radius,extent)

## 第一个参数是radius，也就是半径。
# 当radius值为正数时，圆心在当前画笔（小海龟）左侧；
# 当radius值为负数时，圆心在当前画笔（小海龟）右侧。
## 第二个参数是extent，也就是一个绘制的角度的大小
# 当extent的值为正数时，顺画笔（小海龟）当前方向绘制弧形
# 当extent的值为负数时，逆画笔（小海龟）当前方向绘制弧形
# 重要且应该理解和注意的，当无该参数或参数为None时，绘制整个圆形——相当于默认取值360。

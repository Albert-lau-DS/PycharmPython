# KochDrawV1.py
# 递归函数实现科赫雪花曲线
# 一条长度为n的直线,取其中间的三分之一,将其变为等腰锐角三角形

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
            # 也就是不断地去将该曲线分为三分之一来画，直到最后的是一条直线


def main1():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600, 4)
    turtle.hideturtle()
    turtle.done()  # turtle画完图之后停留在纸面不退出


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3  # 3阶科赫雪花，阶数
    for i in range(1, level+1):
        koch(400, level)
        turtle.right(360/level)
    turtle.hideturtle()
    turtle.done()  # turtle画完图之后停留在纸面不退出


main()

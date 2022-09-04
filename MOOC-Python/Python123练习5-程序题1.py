# Python123练习5-程序题1
# 七段数码管.py

import turtle, time


def drawGap():  # 绘制数码管间隔,让数码管之间有一些间隔,增加美感。
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):  # 绘制单段数码管
    drawGap()  # 开头的间隔
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()  # 结尾的间隔
    turtle.right(90)


def drawDigit(digit):  # 根据数字绘制七段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    # 上述四行代码绘制的是七段数码管的下半部分，回到原点后向海龟左手边旋转90度
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    # 为绘制后续数字确定位置
    turtle.penup()
    turtle.fd(20)


def drawData(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("green")  # 年的部分已经绘制完了，这个颜色是月份的颜色
            turtle.fd(40)
        elif i == "=":
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")  # 月的部分已经绘制完了，这个颜色是日期的颜色
            turtle.fd(40)
        elif i == "+":
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawData(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()

# 答案解析
import turtle as t
import time


def drawGap():  # 绘制数码管间隔
    t.penup()
    t.fd(5)


def drawLine(draw):  # 绘制单段数码管
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)


def drawDigit(d):  # 根据数字绘制七段数码管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)


def drawDate(date):
    t.pencolor("red")
    for i in date:
        drawDigit(eval(i))


def main():
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(time.strftime('%Y%m%d', time.gmtime()))
    t.done()


main()

# 这是本课程的实例7：
#
# 基本思路：
#
#      步骤 1：绘制单个数字对应的码管
#      步骤 2：获得当前系统时间，变成字符串，绘制对应的码管
#
# 思维方法：
#
#      -模块化思维：确定接口，封装功能
#      -规则化思维：抽象过程为规则，计算机自动执行
#      -化繁为简：将大功能变小组合，分而治之

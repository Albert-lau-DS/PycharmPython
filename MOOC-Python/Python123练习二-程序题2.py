# PythonDraw-Practice2
import turtle as t

t.pensize(4)
for i in range(4):
    t.fd(50)
    t.seth(90*(i+1))
t.done()


# 【参考代码】
#RectDraw.py
import turtle as t
t.pensize(2)
for i in range(4):
    t.fd(150)
    t.left(90) # 这里采用了海龟角度，不断往自己的左侧旋转90度
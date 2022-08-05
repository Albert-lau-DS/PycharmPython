# PythonDraw-Practice4
import turtle as t

ANGLE = 100
t.pensize(2)
for i in range(1, 10):
    t.fd(100)
    t.left((180 - ANGLE))
t.done()

# 【参考代码】
#TwoRoundDraw.py
import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(150)
    t.left(80)  #720/9
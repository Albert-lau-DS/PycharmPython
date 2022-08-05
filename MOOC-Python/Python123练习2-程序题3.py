# PythonDraw-Practice3
import turtle as t

t.pensize(2)
for i in range(1, 7):
    t.fd(100)
    t.left(60)  # 也可以采用t.seth(60*i)
t.done()

# 【参考代码】
# HexagonDraw.py
import turtle as t

t.pensize(2)
for i in range(6):
    t.fd(150)
    t.left(60)

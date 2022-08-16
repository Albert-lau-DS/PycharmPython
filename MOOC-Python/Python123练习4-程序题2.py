# 圆周率的计算.py
# 求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，
# 根据在1/4圆内点的数量占总撒点数的比例计算圆周率值。
# 请以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。
import random as ra

ra.seed(123)
Darts = eval(input())
hits = 0.0
for i in range(Darts):
    x, y = ra.random(), ra.random()
    dis = pow(x ** 2 + y ** 2, 0.5)
    if dis < 1:
        hits += 1
pi = 4 * hits / Darts
print("{:.6f}".format(pi))

# 参考代码

from random import random, seed  # 分别在random库中引入函数random和函数seed

DARTS = eval(input())
seed(123)
hits = 0.0
for i in range(DARTS):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
# 需要乘上4来得到整个圆的π值，因此上面求的都是在第一象限中得到的结果，不包含整个圆
print("{:.6f}".format(pi))
# 这是本课程的实例4，请注意：from...import 引入具体的函数，使用seed()需要提前引入

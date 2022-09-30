# 描述
# 输入的三角形的三条边a、b、c 的长度，计算并依次输出三角形的周长和面积，结果严格保留2位小数。
# 测试用例的数据保证三角形三边数据可以构成三角形。 三角形面积计算公式：
# 输入格式：分三行输入 3 个浮点数，表示三角形的三个边长
# 输出格式：周长=xx、面积=xx
import math

a = float(input())
b = float(input())
c = float(input())
s = sum([a, b, c]) / 2
length = sum([a, b, c])
# 这里可以考虑采用for循环来得到结果后再开方(未确定是否正确)
# l = [0,a,b,c]
# length = sum(l)
# s = length/2
# for i in range(l):
#     total = (s-i)*total

area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("周长={:.2f}".format(length))
print("面积={:.2f}".format(area))

## 答案解析

a = eval(input())
b = eval(input())
c = eval(input())
s = (a + b + c) / 2.0
m = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# m=math.sqrt(s * (s - a) * (s - b) * (s - c))    # 第二种开根号方法
print("周长={:.2f}".format(a + b + c))
print("面积={:.2f}".format(m))

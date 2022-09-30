import math
# 描述
# 根据下面公式 avatar
# 计算并输出x的值（保留两位小数），a和b的值由用户输入，括号里的数字是角度值， 要求圆周率的值使用数学常数math.pi，
# 开平方使用math库中开平方函数，三角函数的值用math库中对应的函数进行计算 。
# 输入格式:输入包括两行, 每行一个数字。
# 输出格式:表达式的值
CONSTANT = 60*math.pi/180
a = float(input())
b = float(input())
x = (-b + math.sqrt(2 * a * math.sin(CONSTANT)*math.cos(CONSTANT)))/(2*a)
print('{:.2f}'.format(x))

## 答案解析
import math

a = eval(input())
b = eval(input())
x = (-b+math.sqrt(2 * a * math.sin(math.pi / 3)*math.cos(math.pi / 3)))/(2 * a)
print(x)

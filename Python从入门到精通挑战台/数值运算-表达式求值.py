# 利用下面公式计算并输出 x 的值。
# 输入格式:在 3 行中分别输入一个浮点数（测试数据保证根号下的值大于或等于 0，且a不为零 ）
# 输出格式:一个实数，严格保留小数点后2位数字。
a = float(input())
b = float(input())
c = float(input())
x = (-b + pow((pow(b, 2) - 4 * a * c), 1/2))/(2*a)
print('{:.2f}'.format(x))

## 答案解析
a = float(input())
b = float(input())
c = float(input())
x = (-b + (b * b - 4 * a * c) ** (1 / 2)) / (2 * a)  # (1/2)要加括号，否则幂运算优先级高，（2*a）要加括号
print('{:.2f}'.format(x))
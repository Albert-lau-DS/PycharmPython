# a除以b.py
# 输出实数a除以b的结果，计算结果四舍五入，保留2位小数。
# 输入格式:输入包括两行, 每行一个实数, b不能等于0
# 输出格式:当用户输入b为0时输出"除零错误"
# 其他情况下输出一个保留2位小数的实数

a = eval(input())
b = eval(input())
if b == 0:
    print("除零错误")
else:
    print("{:.2f}".format(a / b))

## 答案解析
# 计算a除以b，结果保留2位小数

a = eval(input())
b = eval(input())
if b != 0:
    print(round(a / b, 2))
else:
    print('除零错误')
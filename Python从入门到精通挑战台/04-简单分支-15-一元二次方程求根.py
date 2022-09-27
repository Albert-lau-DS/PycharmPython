# 一元二次方程求根.py
# 一元二次方程ax2+bx+c=0，a、b、c的值由用户在三行中输入，根据用户输入的数值求解方程的实数解：
# 如果a值 为0，根据b值判断方程是否有解并输出，如果a与b同时为0，则输出Data error!
# 如果方程无实数解，输出“该方程无实数解”；
# 如果方程有两个相同的实数解，输出一个解，结果保留2位小数；
# 如果方程有两个不同的实数解，在一行内按从大到小顺序输出方程的两个解，用空格分隔，结果保留2位小数。
# 输入格式：输入三行数据, 每行输入一个实数
# 输出格式：方程的解
import sympy as sy

x = sy.symbols('x')
a, b, c = eval(input()), eval(input()), eval(input())
if a == 0 and b == 0 and c != 0:
    print("Data error!")
elif pow(b, 2) - 4 * a * c < 0:
    print("该方程无实数解")
else:
    answer = list(sy.solve(a * pow(x, 2) + b * x + c, x))
    if len(answer) == 1:
        print("{:.2f}".format(answer[0]))
    else:
        print("{:.2f} {:.2f}".format(round(max(answer), 2), round(min(answer), 2)))

# 修正版(由于Python123的答案中无法import sympy)
a, b, c = eval(input()), eval(input()), eval(input())
delta = pow(b, 2) - 4 * a * c
if a == 0 and b == 0 and c != 0:
    print("Data error!")
elif a == 0 and b != 0:
    print("{:.2f}".format(-c / b))
elif delta < 0:
    print("该方程无实数解")
elif delta == 0:
    front = pow((pow(b, 2) - 4 * a * c) / (4 * pow(a, 2)), 0.5)
    print("{:.2f}".format(front - b / (2 * a)))
else:
    front = pow((pow(b, 2) - 4 * a * c) / (4 * pow(a, 2)), 0.5)
    answer = list([+front - b / (2 * a), -front - b / (2 * a)])
    print("{:.2f} {:.2f}".format(max(answer), min(answer)))

# 答案解析
a = float(input())
b = float(input())
c = float(input())
delta = b * b - 4 * a * c
if a == 0 and b != 0:
    # print( round(- c / b,2))
    print('{:.2f}'.format(- c / b))
elif a == 0 and b == 0:
    print('Data error!')
elif delta < 0:
    print("该方程无实数解")
elif delta == 0:
    # print(round(-b  / (2 * a),2))
    print('{:.2f}'.format(-b / (2 * a)))
else:
    x1 = (-b + delta ** 0.5) / (a * 2)
    x2 = (-b - delta ** 0.5) / (a * 2)
    if x1 < x2:
        x1, x2 = x2, x1
    # print(round(x1,2),round(x2,2))
    # round()函数获得的浮点数会自动转为最短表示，
    # 例如round(3.10000, 2) 的结果是3.1，而不是3.10
    print('{:.2f} {:.2f}'.format(x1, x2))
    # str.format()的方法可以严格按约定保留小数位数，
    # 例如'{:.2f}'.format(3.100000) 的结果是3.10

# 垫片是在一个圆的中心挖去一个半径小一些的同心圆形成的带孔圆片。
# 用户输入垫片的外圆半径、内孔半径和数量，计算多个垫片的面积之和。
# (圆周率用3.14159，结果保留小数点后2位数字)
# 输入格式
# 第一行输入一个正数，作为外圆半径；
# 第二行输入一个正数，作为内孔半径；
# 第三行输入一个正整数，作为数量；
def is_positive(value):
    value = int(value)
    if value <= 0:
        raise TypeError("%s is an invalid positive int value" % value)
    return value


pi = 3.14159
R_outside = is_positive(int(input()))
R_inside = is_positive(int(input()))
Num = int(input())

area = float((pow(R_outside, 2) - pow(R_inside, 2)) * pi * Num)

print("{:.2f}".format(area))# 或者 print('f{area:.2f}')

## 答案解析
PI = 3.14159  # 定义Pi值精确度
R = float(input())  # 输入外圆半径R
r = float(input())  # 输入内孔半径r
n = int(input())  # 输入数量n
area_of_sum = n * (PI * R * R - PI * r * r)  # 计算总面积
print('{:.2f}'.format(area_of_sum))  # 格式化输出
# 或
# print(f'{area_of_sum:.2f}')        # 格式化输出

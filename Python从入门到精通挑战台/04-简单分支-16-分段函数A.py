# 分段函数A.py
# ![](C:/Users/80549/AppData/Local/Temp/f312f8a5b0da5a0186613c847f9e.png)
# 按照上面的分段函数，对输入的整数x，输出对应的y值。对于超出范围的整数x，输出“ERROR”。
# 本题保证测试数据中x均为整数。
# 输入格式:输入一个整数，表示x的值
# 输出格式:输出y的值或者“ERROR”

x = int(input())
if -10 <= x < 0:
    print("{:.0f}".format(2 * x ** 3 + 4 * x ** 2 + 3))
elif 0 <= x < 6:
    print("{:.0f}".format(x + 14))
elif 6 <= x <= 10:
    print("{:.0f}".format(6 * x))
else:
    print("ERROR")

x = int(input())
if x > 10 or x < -10:
    print("ERROR")
else:
    if 0 <= x < 6:
        y = x + 14
    elif 6 <= x <= 10:
        y = 6 * x
    else:
        y = 2 * x * x * x + 4 * x * x + 3
    print(y)
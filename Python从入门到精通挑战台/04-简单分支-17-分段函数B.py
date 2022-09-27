# ![](C:/Users/80549/AppData/Local/Temp/e87c0b66b86259aa1e6d82737617.png)
# 按照输入的整数x，输出对应的y值。本题保证所有测试用例均在整数范围内。
# 输入格式：输入一个整数，表示x的值
# 输出格式：输出y的值
def b(x):
    if -6 <= x < 0:
        y1 = abs(x) + 5
    elif 0 <= x < 3:  # 8-14行直接求阶乘，没有采用math库来求阶乘
        if x == 0:
            y1 = 1
        else:
            y1 = 1
            for i in range(1, x + 1):
                y1 *= i
    elif 3 <= x <= 6:
        y1 = pow(x, (x - 2))
    else:
        y1 = 0
    return y1


y = b(int(input()))
print(y)

# 答案解析
import math  # 引入了math库，使用factorial函数来求阶乘

x = int(input())
if x > 6 or x < -6:
    y = 0
elif 0 <= x < 3:
    y = math.factorial(x)
elif 3 <= x <= 6:
    y = pow(x, x - 2)
else:
    y = abs(x) + 5
print(y)

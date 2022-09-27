# 计算整数 n 的阶乘.py
# 输入一个数值，如果输入的数据为浮点数或者负数，输出”ERROR“，否则计算输入的数的阶乘并输出。
# 输入格式：输入一个数值
# 输出格式：输出其阶乘或“ERROR”
import math

num = eval(input())
print(math.factorial(num)) if (type(num) == int and num >= 0) else print("ERROR")

# 答案解析
# 逻辑分支式
import math

n = eval(input())
if n >= 0 and type(n) == int:
    print(math.factorial(n))
else:
    print("ERROR")


import math

n = eval(input())
if isinstance(n, int) and n >= 0:  # isinstance(i, int)函数为判断i是否为正整数，通过该函数还可以判断其他类型的数据。
    print(math.factorial(n))
else:
    print("ERROR")

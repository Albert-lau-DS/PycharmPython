# 阶乘求和.py
# 输入一个正整数n，计算 1!+2!+3!+...+n! 的和并输出。
# 输入一个正整数n
# 输出从1到n每个数的阶乘的和
import math

count = 0
n = int(input())+1
for i in range(1, n):
    count = count+math.factorial(i)
print(count)

## 答案解析

# 计算1！+2！+3！+。。。+n!
def sum_factorial(n):
    total, t = 1, 1
    for i in range(2, n + 1):
        t = t * i
        total = total + t
    return total


n = int(input())
print(sum_factorial(n))


n = int(input())
# 函数式编程
def factorial(n):  # 阶乘函数
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def sum_factorial1(n):  # 累加函数
    total = 0
    for i in range(1, n + 1):
        total = total + factorial(i)
    return total


print(sum_factorial1(n))
# 使用内置函数更简单，但效率略低，规模大时有体现
# from math import factorial
# print(sum(map(factorial,range(1,n+1))))
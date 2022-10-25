# 计算阶乘.py
# 用户输入一个非负整数 n，计算并输出其阶乘。
# n!=1×2×3×...×n.
# 输入一个非负整数 n
# 输出n 的阶乘

n = int(input())
s = 1
for i in range(1, n+1):
    s = s*i
print(s)

## 答案解析
#用户输入一个正整数，计算其阶乘
import math
#print(math.factorial(eval(input())))

n = int(input())
fact = math.factorial(n) # 采用factorial函数来实现阶乘
print(fact)

fact = 1
n = int(input())
for i in range(1, n + 1):
    fact = fact * i
print(fact)
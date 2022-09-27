# 描述
# 一个正整数如果等于组成它的各位数字的阶乘之和，则该正整数称为阶乘和数。
# 例如正整数145，1!+4!+5!等于145，因此145就是一个阶乘和数。输入一个正整数，
# 计算它的各位数字的阶乘之和，判断它是否是一个阶乘和数。
# 当输入的数字为阶乘和数时，输出“YES”,否则输出“NO”。注意：输入的正整数的最高位不为0。
# 输入格式：一个正整数。
# 输出格式：输出字符串“YES”或“NO”

import math

def cal(n):
    m = str(n)
    count = 0
    for i in range(len(m)):
        count += math.factorial(eval(m[i]))
    return count == n


num = eval(input())
print('YES') if cal(num) else print('NO')


# 答案解析
# 正整数145，1!+4!+5!等于145
import math

# 循环解法
# n = input()
# total = 0
# for i in n:
#     total = total + math.factorial(int(i))
# print(total)
# if int(n) == total:
#     print('YES')
# else:
#     print('NO')

import math

n = input()
s = sum(math.factorial(int(i)) for i in n)  # 推导式
if int(n) == s:
    print('YES')
else:
    print('NO')

# 这一句需要特别去学习！！！
# s = sum(math.factorial(int(i)) for i in n)  # 推导式
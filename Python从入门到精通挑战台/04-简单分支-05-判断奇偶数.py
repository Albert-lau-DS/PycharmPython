# 判断奇偶数.py
# 用户输入一个正整数，判断该数是奇数还是偶数，如果奇数输出odd，偶数则输出even。
# 输入格式:输入一个正整数
# 输出格式:奇数输出odd，偶数则输出even。

num = int(input())
print("even") if (num % 2 == 0) else print("odd")

# 答案解析

# 用户输入一个整数，判断该数是奇数还是偶数，如果奇数输出odd，偶数则输出even
number = int(input())
if number % 2 == 1:
    print("odd")
else:
    print("even")

# 条件表达式解法
# number = int(input())
# print("odd") if number % 2 == 1 else print("even")
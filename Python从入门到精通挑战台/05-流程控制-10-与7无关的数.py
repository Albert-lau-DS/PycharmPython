# 描述
# 一个正整数，如果它能被7整除，或者它的十进制表示法中某一位的数字为7，则称其为与7相关的数、
# 求所有小于n(n < 100)的与7无关的正整数以及他们的平方和。
#
# 输入格式：输入为一个正整数
# 输出格式：两行 第一行为所有与7无关的数，以列表形式输出，逗号分开 第二行为他们的平方和

# num = int(input())
# ls = []
# count = 0
# for i in range(1, num+1):
#     if not (i % 10 == 7 or i//10 == 7):  # 没有考虑到能被7整除的情况
#         # 需要再加上 i%7 == 0的情况
#         ls.append(i)
#         count += pow(i, 2)
# print(ls)
# print(count)

# 修正版
num = int(input())
ls = []
count = 0
for i in range(1, num):
    if not (i % 10 == 7 or i//10 == 7 or i % 7 == 0):
        ls.append(i)
        count += pow(i, 2)
print(ls)
print(count)


## 答案解析
n = int(input())
total = 0
ls = []
for i in range(n):
    if not (i % 7 == 0 or i % 10 == 7 or i // 10 == 7):
        total = total + i * i  # 计算平方和
        ls.append(i)  # 往列表里塞满足条件的数
print(ls)
print(total)
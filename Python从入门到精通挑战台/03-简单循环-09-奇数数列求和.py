# 奇数数列求和.py
# 输入一个正整数 n，求数列1，3，5，……，（2n-1）的前n项的和。
# 输入一个正整数 n
# 输出数列的和

n = int(input())
num = 0
my_sum = 0
for i in range(1, n+1):
    num = 2*i-1
    my_sum = my_sum+num
print(my_sum)

## 答案解析

n = int(input())
print(sum(range(1,2*n,2)))     # 步长为2
# 这里直接在range里面取步长为2，由1开始加起，直到2n-1就停止，然后直接把range里面的数值sum求和
#或

#求1+3+5+……+（2n-1）前n项和
n = int(input())
sum = 0
for i in range(1,n + 1):
    sum = sum + (2 * i - 1) # 将第10/11行综合起来，在计算的同时直接相加
print(sum)
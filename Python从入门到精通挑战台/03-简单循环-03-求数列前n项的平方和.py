# sum_of_the_squares.py
# Find the sum of the squares of the first n terms of the sequence
# 现有数列：1，2，3，4，……，n，计算并输出其前n项的平方和，即求：
# 1×1＋2×2＋3×3＋……＋n×n的和。

n = int(input())+1
sums=0
for i in range(n):
    s = i**2
    sums = s+sums # 这里可以将9/10行合并为一行 sums = sum+i**2
print(sums)


## 答案解析

#1×1＋2×2＋3×3……的前n项和

n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + i * i
print(sum)

# 整数的加减和.py
# 编写程序计算如下数列的值：1-2+3-4...966
# 其中，所有数字为整数，从1开始递增，奇数为正，偶数为负

# 常规版
n = 966
s = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        s += i
    else:
        s -= i
print("{:.0f}".format(s))


# 函数版
def summary(n):  # 由0开始计算，从+1到+-n
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            s += i
        else:
            s -= i
    return s


s = summary(966)
print("{:.0f}".format(s))

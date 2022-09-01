# 递归函数实现斐波那契数列
def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1)+F(n-2)


print(F(6))
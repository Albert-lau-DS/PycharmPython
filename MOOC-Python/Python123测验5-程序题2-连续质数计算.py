# 连续质数计算.py
# 描述
# 补充编程模板中代码，完成如下功能：
# 获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。
# 注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。

# 请在...补充一行或多行代码

def prime(m):
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_ + 1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1
    n_ += 1
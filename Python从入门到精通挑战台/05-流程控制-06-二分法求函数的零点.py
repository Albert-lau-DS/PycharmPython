# 描述
# 现有方程：f(x) = x5-15x4+85x3-225x2+274x-121,
# 已知f(x)在[1.5,2.4]区间单调下降，且在该区间f(x)==0有且只有一个根，用二分法求解该根。
# 输入格式：输入一个正整数n，当f(x)值小于10-n时认为函数值为0
# 输出格式：输出方程在[1.5,2.4]区间的根，精确到小数点后第6位

# 这里打算用迭代的方式去实现不断缩小范围的功能
# def compare(x1, x2, x):
#     x3 = (x1+x2)/2
#     y3 = myfun(x3)
#     while abs(y3) >= x:
#         if y3 > 0:
#             x1 = x3
#             x2 = x2
#             compare(x1, x2, x)
#         else:
#             x1 = x1
#             x2 = x3
#             compare(x1, x2, x)
#     return x3
def compare(x1, x2, x):
    while True:
        mid = (x1+x2)/2
        if abs(myfun(mid)) < x:
            return mid
        elif myfun(mid) > 0:
            x1 = mid
        else:
            x2 = mid


def myfun(x):
    y = pow(x, 5)-15*pow(x, 4)+85*pow(x, 3)-225*pow(x, 2)+274*x-121
    return y


threshold = pow(10, -int(input()))
print("{:.6f}".format(compare(1.5, 2.4, threshold)))


# 答案解析
def f(x):
    return x ** 5 - 15 * x ** 4 + 85 * x ** 3 - 225 * x ** 2 + 274 * x - 121


def bisection_method(low, high):
    while True:
        mid = (low + high) / 2
        if abs(f(mid)) < 1 * 10 ** -n:
            return '{:.6f}'.format(mid)
        elif f(mid) < 0:
            high = mid
        else:
            low = mid


if __name__ == '__main__':  # 这里的if __name__ == '__main__':是什么意思？
    n = int(input())
    Low, High = 1.5, 2.4
    print(bisection_method(Low, High))

# if __name__ == '__main__': 的解释如下：
# https://blog.csdn.net/heqiang525/article/details/89879056
# 为的是在脚本内被执行，如果不是在该脚本中执行而是被import的话就不被执行
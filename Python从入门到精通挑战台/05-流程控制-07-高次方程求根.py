# 描述
# 有函数 https://python123.io/images/d4/69/f610531327711586cca12fb51169.png
# 已知f(1.5)>0,f(2.4)<0，且在[1.5,2.4]区间只且只有一个根，
# 求该根（假定多项式值小于10-6时可近似为0）。要求四舍五入到小数点后6位
# 输入格式：无
# 输出格式：该方程在[1.5,2.4]区间的根
def dichotomy(left, right):
    n = 1e-6
    count = 1
    while True:
        mid = (left+right)/2
        count += 1
        if abs(fun(mid)) < n:
            return mid
        elif fun(mid) > 0:
            left = mid
        else:
            right = mid


def fun(x):
    y = pow(x, 5)-15*pow(x, 4)+85*pow(x, 3)-225*pow(x, 2)+274*x-121
    return y


if __name__ == '__main__':
    left, right = 1.5, 2.4
    print("{:.6f}".format(dichotomy(left, right)))


## 答案解析(与上一题几乎是一样的)
def f(x):
    # 这个函数用来计算这个多项式
    return x ** 5 - 15 * x ** 4 + 85 * x ** 3 - 225 * x ** 2 + 274 * x - 121


x1, x2 = 1.5, 2.4
while abs(f((x1 + x2) / 2)) > 1e-6:
    # 二分法，如果大于0调整下界，反之调整上界
    if f((x1 + x2) / 2) > 0:
        x1 = (x1 + x2) / 2
    else:
        x2 = (x1 + x2) / 2
print("{:.6f}".format((x1 + x2) / 2))

# 采用牛顿法来求解
# import math

# def newton(convergence, ini_root):
#     print('current acceptable error: ' + str(convergence) + '\n')
#     error = convergence + 1  #循环开始条件
#     cur_root = ini_root
#     count = 1  # 迭代计数
#     while error > convergence:
#         print(str(count) + ' root = ' +str(cur_root))
#         func = math.exp(cur_root) * math.log(cur_root) - cur_root**2
#         dif_func = math.exp(cur_root) * ((1 / cur_root) + math.log(cur_root)) - 2 * cur_root
#         cur_root = cur_root - func / dif_func # 进行迭代
#         error = abs(func)  # 计算误差
#         count += 1
#
# convergence = float(input("your acceptable error:"))
# ini_root = float(input('your initial root '))
# newton(convergence, ini_root)
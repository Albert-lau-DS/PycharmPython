def division(m, n):
    """接收两个整数 m 和 n为参数，
    第一行输出 m 对 n 做整除的结果。
    第二行输出m 除以 n 的结果。
    函数没有返回值。
    """
    print("{}\n{}".format(int(a/b),a/b))


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    division(a, b)  # 调用函数计算除法

## 答案解析
def division(m, n):
    """接收两个整数 m 和 n为参数，
    第一行输出 m 对 n 做整除的结果。
    第二行输出m 除以 n 的结果。
    函数没有返回值。
    """
    print(m // n)  # m 对n 整除
    print(m / n)  # m 除以n


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    division(a, b)  # 调用函数计算除法
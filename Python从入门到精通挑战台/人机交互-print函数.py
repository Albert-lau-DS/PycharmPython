"""
描述
输入一个正整数 n，在一行中输出从 1到 n，中间无空格。
输入格式
输入一个正整数 n
输出格式
在一行中输出从 1 到 n，中间无空格
"""


def s_num(n):
    for i in range(n):
        i = i+1
        print(i,end='')


if __name__ == '__main__':
    n = int(input())  # 输入一个正整数
    s_num(n)  # 调用函数

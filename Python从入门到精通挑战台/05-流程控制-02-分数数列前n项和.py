# 描述
# 输入一个正整数 n, 计算并输出数列1、-1/2、2/3、-3/5、4/8、-5/12...的前n项和。
# 输入格式：输入一个正整数 n
# 输出格式：以浮点数形式输出数列前n项的和

def summary(n):
    count = 0.0
    if n == 1:
        count += n
    else:
        a = 1
        b = 1
        for i in range(n):
            count += pow(-1, i) * a/b
            a, b = b, a+b  # 出错的地方在这里，没有了解题意，分子是等差递增的
    return count


n = eval(input())
if n != int(n):
    print('data error!')
else:
    print(summary(n))


# 答案解析
n = int(input())
a, b = 1, 2
flag = -1
result = 1.0
for i in range(1, n):
    result = result + flag * a / b
    a, b = i + 1, a + b
    flag = -flag
print(result)

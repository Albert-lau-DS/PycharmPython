# 星号三角形
# 读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：
# 第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。
n = int(input())
if n // 2 == 0:
    n += 1
for i in range(1, n+1, 2):
    a = '*'*i
    print(a.center(n, " "))# 该代码无法解答n=1的情况
    ## 思考！
    # 由于输入1之后，n//2==0，因此会加上自加，所以会变为两个占位符

# 修正版
n = int(input())
if n + 2 // 2 == 0:
    n += 1
for i in range(1, n+1, 2):
    a = '*'*i
    print(a.center(n, " "))

# 参考答案

n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))  # 通过{}.format 槽的机制来放入*

# 关键是对.format()中槽机制的理解，槽中可以嵌套槽，用来表示宽度、填充等含义。
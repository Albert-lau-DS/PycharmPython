import math
def loop(n):
    for i in range(n):
        print(pow(i,2))
if __name__ == '__main__':
    n = int(input())  # 输入一个整数
    loop(n)  # 调用函数运算

## 答案解析
n = int(input())        # 输入转为整数n
for i in range(n):      # 将i从0遍历到n
    print(i * i)        # 输出i的平方

# 函数式编程
def loop(n):
    for i in range(n):    # 将i从0遍历到n
        print(i * i)      # 输出i的平方

if __name__ == '__main__':
    n = int(input())       # 输入转为整数n
    loop(n)                # 调用你定义的loop函数并传入参数n
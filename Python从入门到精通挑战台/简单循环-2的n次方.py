# 2的n次方
# 计算并输出 2 的 n 次方，n 由用户输入 。
# 输入一个非负整数 n
# 以整数类型输出2的 n 次方

n = int(input())
print(int(2**n))

## 答案解析
n = eval(input())
print(pow(2,n))   #pow(x,y[,z])同x**y%z，常省略z,用于计算x的y次方
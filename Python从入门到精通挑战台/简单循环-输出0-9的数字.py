# print_number.py
num = input()
for i in range(eval(num)):
    print(i, end=' ')

## 答案解析
n=int(input()) # 要加一个int 强制输入为整数

for i in range(n):
    print(i,end=' ')
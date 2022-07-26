# sum.py
# 描述
# 输入一个正整数 n ，计算从 1 到 n 各数字的和，要求用一行代码实现。
print(sum(range(int(input()) + 1)))

## 答案解析
# 通过range 函数生成1到输入的数的整数序列
# 通过sum 函数对序列求和
print(sum(range(1, int(input()) + 1)))

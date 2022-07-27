# 分数序列求和.py
# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前 n 项之和, n 由用户输入。
# 输入一个正整数
# 输出前n项和

n = int(input())
mole = {}
den = {}
Fraction = 0
mole[1] = 2
den[1] = 1
if n == 1:
    print(mole[1]/den[1])
else:
    for i in range(2, n+1):
        mole[i] = mole[i-1]+den[i-1]
        den[i] = mole[i-1]
        Fraction = mole[i]/den[i]+Fraction
    my_sum = Fraction+mole[1]/den[1]
    print(round(my_sum, 3))

## 答案解析

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前n项之和,n由用户输入。
# 除了首项，分子为前一项分子分母之和，分母为前一项分子
n = int(input())
sum_of_n = 0
a, b = 2, 1
for i in range(1, n + 1):
    sum_of_n = sum_of_n + a / b
    # 先把数值加上，然后再进行数值的变换，这样可以避免更换后的数值跳过第二行
    b, a = a, a + b  # 30/31行精髓！
print(round(sum_of_n, 3))
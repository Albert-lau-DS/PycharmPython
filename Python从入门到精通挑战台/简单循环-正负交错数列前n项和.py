# 正负交错数列前n项和.py
# 1-1/2+2/3-3/5+4/8-5/13+...的前n项和，n由用户输入（n>0）
# 结果用str.format()方法保留小数点后6位数字输出。
# 输入一个正整数
# 输出前n项的和

n = int(input())
mole, den = 1, 1
mole1, den1 = 1, 1
count = 0
if n == 1:
    print('{:.6f}'.format(mole / den))
else:
    for i in range(2, n + 1):
        num = (i - 1) / (mole + den)
        mole, den = den, mole + den
        # 这里设置a,b=c,d可以同步提取上一个的mole和den，避免混淆
        if i % 2 == 0:
            my_num = -1 * num
        else:
            my_num = 1 * num
        count = count + my_num
    total = count + mole1 / den1
    print('{:.6f}'.format(total))

## 答案解析
# 分析：
# 分子规律为：1，1，2，3，4，5，...，除首个数字外是自然数
# 分母规律为：1，2，3，5，8，13...，除首个数字外，后面每个数是前面两个数的加和
# 符号规律：正负交替
# 项数：1，2，3，...n共n项
# previous, current = 1, 1
#    1          2        1         1    +    1
# previous, current = current, previous + current

# previous, current = 1, 2
#    2          3        2         1    +    2
# previous, current = current, previous + current

# previous, current = 2, 3
#    3          5        3         2    +    3
# previous, current = current, previous + current
# previous, current = 3, 5
# ......

n = int(input())
result = 1  # 首项的值，作为累加初值
sign = -1  # 符号，第二项是负值，
previous, current = 1, 1  # 分母数字的初值，从第二项开始符合这个规律
for i in range(1, n):  # 从1到n-1遍历n-1次
    previous, current = current, previous + current  # 下一个数值是前面两个数的加和
    result = result + sign * i / current  # 注意分子是 i
    sign = -sign  # 改变正负号
print('{:.6f}'.format(result))

# sign*i就可以判断正负号了
# 重要知识！！！
# for i in range(1,1)会直接跳出循环，不执行for以内的操作。
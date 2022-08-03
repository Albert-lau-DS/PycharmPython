# DayDayUpQ3.py
# 将数学思维转变为计算机程序思维，当遇到工作日进步dayfactor，当遇到休息日下降dayfactor
# for..in..(计算思维)
dayup = 1.0
dayfactor = 0.01
daynum = 365
week = 7

for i in range(daynum):
    if i % week in [6, 0]:  # if i % week == 6 or i % week == 0: 的简写，须记住。
        dayup = dayup * (1 - dayfactor)  # 基础努力减去进步变量
    else:
        dayup = dayup * (1 + dayfactor)
print("工作日的力量:{:.2f}".format(dayup))

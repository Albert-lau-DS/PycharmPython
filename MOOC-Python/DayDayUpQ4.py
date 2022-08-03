# DayDayUpQ4.py
# 工作日模式下要努力到什么水平，才能与每天努力1%一样？
# A：一年365天，每天进步1%
# B：一年365天，每周工作日进步休息日下降，且休息日下降1%，则工作日需要进步多少？
# def..while..(笨办法，试错)
dayUp = 1.0
dayfactor_A = 0.01
daynum = 365
dayup_A = pow((dayUp + dayfactor_A), daynum)


def dayUP(df):  # 每次的def函数结束后，需要换行两行，再进行代码编写
    dayup = 1.0
    daynum = 365
    week = 7

    for i in range(daynum):
        if i % week in [6, 0]:  # if i % week == 6 or i % week == 0: 的简写，须记住。
            dayup = dayup * (1 - 0.01)  # 这里的0.01是固定的退步1%
        else:
            dayup = dayup * (1 + df)  # 这里的df就是输入的dayfactor
    return dayup


dayfactor = 0.01
while dayUP(dayfactor) < dayup_A:  # 把dayUP函数得到的结果dayup与dayup_A进行比较
    dayfactor += 0.001  # 进步步长
print("工作日的努力参数是:{:.3f}".format(dayfactor))
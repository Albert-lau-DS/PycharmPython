# 天天向上的力量.py
# 工作日模式要努力到什么水平，才能与每天努力1%一样？
# -A君: 一年365天，每天进步1%，不停歇
# -B君: 一年365天，每周工作5天休息2天，休息日下降1% ，要多努力呢？
# 每周工作5天休息2天，计算工作日的努力参数是多少才能与每天努力1%一样。

# daydayup

daybase = 1.0
dayfactor = 0.01
daynum = 365
dayup_A = pow((daybase + dayfactor), daynum)


def mydayupfun(df):
    dayup_B = 1.0
    week = 7

    for i in range(daynum):
        if i % week in [6, 0]:
            dayup_B *= (1 - dayfactor)
        else:
            dayup_B *= (1 + df)
    return dayup_B


dayfactor_B = 0.01
dayup_B_L = 0.001
while mydayupfun(dayfactor_B) < dayup_A:
    dayfactor_B += dayup_B_L
print("工作日的努力参数是: {0:.3f}".format(dayfactor_B))

## 参考代码

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是: {:.3f}".format(dayfactor))

# (1) 工作日模式，每天要努力到1.9%，相当于365模式每天1%的；
# (2) 采用{:.3f}将输出数字变成三位小数点表示时
#     即使数学上该输出值是整数，也会按照小数方式输出。

### 采用自加或者自乘的方式可以简化代码
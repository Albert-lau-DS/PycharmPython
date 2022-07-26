# 在三行中依次输入初始存款金额，存款年限，年利率。
# 每年末计一次利息并转为本金，计算并输出存款到期时的利息（不含本金，税前），结果保留2位小数。
# 复利法,每年末计算利息并自动转存：
# F=P×(1+i)N
# F：复利终值
# P：本金
# i：利率
# N：利率获取时间的整数倍(年限)
P = int(input())
N = int(input())
i = float(input())

F = P * pow((1 + i), N) - P
print('利息={:.2f}'.format(F))

## 答案解析
# 循环运算实现
deposit = int(input())  # 存款金额本金
years = int(input())    # 存款年数
interest_rates = float(input())  # 年利率
new_deposit = deposit            # 初始本金
for i in range(years):           # 逐年计算新的一年的本息合计
    new_deposit = new_deposit*(1 + interest_rates)  # 每年的本息合计总收益
interest = new_deposit - deposit  # 总收益中去掉初始本金结果为利息
print("利息={:.2f}".format(interest))

# 幂运算实现
deposit = int(input())  # 存款金额本金
years = int(input())
interest_rates = float(input())
total = deposit * pow((1 + interest_rates), years)
interest = total - deposit
print("利息={:.2f}".format(interest))
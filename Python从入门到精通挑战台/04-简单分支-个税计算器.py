# 个税计算器.py
# 目前我国个人所得税计算公式如下：
# 应纳个人所得税税额= (工资薪金所得 -五险一金 - 个税免征额)×适用税率-速算扣除数
# 个税免征额为5000元/月，2018年10月1日起调整后，
# 也就是2018年实行的7级超额累进个人所得税税率表如下：
# 全月应纳税所得额（含税级距）  税率(%)   速算扣除数
# 不超过3,000元               3             0
# 超过3,000元至12,000元的部分  10           210
# 超过12,000元至25,000元的部分 20         1,410
# 超过25,000元至35,000元的部分 25         2,660
# 超过35,000元至55,000元的部分 30         4,410
# 超过55,000元至80,000元的部分 35         7,160
# 超过80,000元的部分          45         15,160
# 请编写一个个税计算器，
# 用户输入为应发工资薪金所得扣除五险一金后的金额，输出应缴税款和实发工资，
# 结果保留小数点后两位。当输入数字小于0时，输出“error”。

# 常规版
# wx = 0
# tax = float()
# pay = eval(input()) - wx
# personal_income = [0, 3e3, 12e3, 25e3, 35e3, 55e3, 80e3]
# exemption = 5000
# tax_rate = [3e-2, 10e-2, 20e-2, 25e-2, 30e-2, 35e-2, 45e-2]
# Quick_de = [0, 210, 1410, 2660, 4410, 7160, 15160]
# tax_full = [(personal_income[1]-personal_income[0]) * tax_rate[0],
#             (personal_income[2]-personal_income[1]) * tax_rate[1],
#             (personal_income[3]-personal_income[2]) * tax_rate[2],
#             (personal_income[4]-personal_income[3]) * tax_rate[3],
#             (personal_income[5]-personal_income[4]) * tax_rate[4],
#             (personal_income[6]-personal_income[5]) * tax_rate[5]]
# if pay < 0:
#     print('error')
# elif 0 <= pay <= exemption + personal_income[0]:
#     tax = 0
# elif exemption + personal_income[0] < pay <= exemption + personal_income[1]:
#     tax = (pay - personal_income[0]) * tax_rate[0] + Quick_de[0]
# elif exemption + personal_income[1] < pay <= exemption + personal_income[2]:
#     tax = (pay - personal_income[1]) * tax_rate[1] + Quick_de[1] + tax_full[0]
# elif exemption + personal_income[2] < pay <= exemption + personal_income[3]:
#     tax = (pay - personal_income[2]) * tax_rate[2] + Quick_de[2] + tax_full[1]
# elif exemption + personal_income[3] < pay <= exemption + personal_income[4]:
#     tax = (pay - personal_income[3]) * tax_rate[3] + Quick_de[3] + tax_full[2]
# elif exemption + personal_income[4] < pay <= exemption + personal_income[5]:
#     tax = (pay - personal_income[4]) * tax_rate[4] + Quick_de[4] + tax_full[3]
# elif exemption + personal_income[5] < pay <= exemption + personal_income[6]:
#     tax = (pay - personal_income[5]) * tax_rate[5] + Quick_de[5] + tax_full[4]
# else:
#     tax = (pay - personal_income[6]) * tax_rate[6] + Quick_de[6] + tax_full[5]
#
# earn = pay - tax
# print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(tax, earn))

# 常规修正版
Five_one = 0
exemption = 5000
salary = eval(input())
personal_income = [0, 3e3, 12e3, 25e3, 35e3, 55e3, 80e3]
tax_rate = [0, 3e-2, 10e-2, 20e-2, 25e-2, 30e-2, 35e-2, 45e-2]
Quick_de = [0, 0, 210, 1410, 2660, 4410, 7160, 15160]
if salary < 0:
    print('error')
else:
    tax_salary = salary - exemption
    if tax_salary <= personal_income[0]:
        fee, num = tax_rate[0], Quick_de[0]
    elif tax_salary <= personal_income[1]:
        fee, num = tax_rate[1], Quick_de[1]
    elif tax_salary <= personal_income[2]:
        fee, num = tax_rate[2], Quick_de[2]
    elif tax_salary <= personal_income[3]:
        fee, num = tax_rate[3], Quick_de[3]
    elif tax_salary <= personal_income[4]:
        fee, num = tax_rate[4], Quick_de[4]
    elif tax_salary <= personal_income[5]:
        fee, num = tax_rate[5], Quick_de[5]
    elif tax_salary <= personal_income[6]:
        fee, num = tax_rate[6], Quick_de[6]
    else:
        fee, num = tax_rate[7], Quick_de[7]
    tax = tax_salary * fee - num
    earn = salary - tax
    print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(tax, earn))

# 函数版
def tax_cal(salary):
    return 0
# 答案解析
s = float(input())
# 先判断输入是正数，然后根据输入的工资范围定税率和速算扣除数
if s < 0:
    print("error")
else:
    salary = s - 5000
    if salary <= 0:
        fee, num = 0, 0
    elif salary <= 3000:
        fee, num = 3, 0
    elif salary <= 12000:
        fee, num = 10, 210
    elif salary <= 25000:
        fee, num = 20, 1410
    elif salary <= 35000:
        fee, num = 25, 2660
    elif salary <= 55000:
        fee, num = 30, 4410
    elif salary <= 80000:
        fee, num = 35, 7160
    else:
        fee, num = 45, 15160
    tax = abs(salary * fee / 100 - num)
    print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(tax, salary + 5000 - tax))

# 答案解析
s = float(input())
# 先判断输入是正数，然后根据输入的工资范围定税率和速算扣除数
if s < 0:
    print("error")
else:
    salary = s - 5000
    if salary <= 0:
        fee, num = 0, 0
    elif salary <= 3000:
        fee, num = 3, 0
    elif salary <= 12000:
        fee, num = 10, 210
    elif salary <= 25000:
        fee, num = 20, 1410
    elif salary <= 35000:
        fee, num = 25, 2660
    elif salary <= 55000:
        fee, num = 30, 4410
    elif salary <= 80000:
        fee, num = 35, 7160
    else:
        fee, num = 45, 15160
    tax = abs(salary * fee / 100 - num)
    print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(tax, salary + 5000 - tax))
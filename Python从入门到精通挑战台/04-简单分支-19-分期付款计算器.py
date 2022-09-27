# 分期付款计算器.py
# 描述:购买房屋或大宗家电时，很多时候可以分期付款，还款方式分为等额本息和等额本金两种：
# 等额本息（Average Capital Plus Interest:ACPI）还款公式:
# 每月还款额=贷款本金*月利率*(1+月利率)**总还款月数/((1+月利率)**总还款月数-1)
# 等额本金（Average Capital:AC）还款公式:
# 每月还款额=贷款本金/总还款月数+(贷款本金-累计已还款本金)*月利率
# 设计一个程序计算分期付款时每一期的应还款额，还款方式输入错误时，输出“还款方式输入错误”。
# 输入格式:4行输入：
# 第1行输入一个浮点数，表示贷款本金
# 第2行输入一个整数，表示分期月数
# 第3行输入一个字符串，表示还款方式，限定只能输入"ACPI"或"AC"，分别表示等额本息和等额本金
# 第4行输入一个浮点数，表示月利率
# 输出格式:输出每月还款额，等额本金方式时，输出的数字间用逗号分隔(用round()函数保留2位小数)
# 还款方式输入错误时，输出“还款方式输入错误”
def ACPI(dkbj, fqys, myll):
    # 等额本息（Average Capital Plus Interest:ACPI）还款公式:
    # 每月还款额=贷款本金*月利率*(1+月利率)**总还款月数/((1+月利率)**总还款月数-1)
    money1 = dkbj*myll*(1+myll)**fqys/((1+myll)**fqys-1)
    money1 = round(money1, 2)
    return money1


def AC(dkbj, fqys, myll):
    # 等额本金（Average Capital:AC）还款公式:
    # 每月还款额=贷款本金/总还款月数+(贷款本金-累计已还款本金)*月利率
    count = 0.0
    money_ = []
    for i in range(1, fqys+1):
        money2 = dkbj/fqys + (dkbj-count)*myll
        money_.append(money2)
        count = count + money2
    money__ = []
    for num in money_:
        nums = round(num, 2)
        money__.append(nums)
    return money__


loan_dkbj = eval(input("请输入贷款本金:"))
loan_fqys = eval(input("请输入分期月数:"))
loan_hkfs = input("请输入还款方式(限定只能输入ACPI或AC,分别表示等额本息和等额本金):")
loan_myll = eval(input("请输入月利率:"))

if loan_hkfs == 'ACPI' or loan_hkfs == 'acpi':
    num = ACPI(loan_dkbj, loan_fqys, loan_myll)
    print("{}".format(num))
elif loan_hkfs == 'AC' or loan_hkfs == 'ac':
    num = AC(loan_dkbj, loan_fqys, loan_myll)
    print("{}".format(num))
else:
    print("还款方式输入错误")


# 答案解析
price,month,mode,rate = float(input()),int(input()),input(),float(input())
if mode == 'AC':
    ls = []
    for i in range(month):
        # 这里可以采用price / month * i来表示每月偿还的贷款
        repayment = price / month + (price - price / month * i) * rate
        ls.append(round(repayment,2))
    print(ls)
elif mode == 'ACPI':
    repayment = price * rate * (1 + rate) ** month /((1 + rate) ** month - 1)
    print(round(repayment,2))
else:
    print('还款方式输入错误')
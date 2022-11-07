# Python网络爬虫与信息提取 练习实例2.py
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时,高于20万元的部分，可提成5%；
# 40万到60万之间时,高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
#
# 程序分析：请利用数轴来分界，定位。
I = float(input("请输入利润(元):"))
arry = [1e5, 2e5, 4e5, 6e5, 10e5]
rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.001]
bonu = [arry[0] * 0.1, (arry[1] - arry[0]) * 0.075, (arry[2] - arry[1]) * 0.05,
        (arry[3] - arry[2]) * 0.03, (arry[4] - arry[3]) * 0.015]
if I <= arry[0]:
    bonus = I * rate[0]
    print("奖金总数为:{0:.2f}".format(bonus))
elif arry[0] < I <= arry[1]:
    bonus = (I - arry[0]) * rate[1] + sum(bonu[0:1])
    print("奖金总数为:{0:.2f}".format(bonus))
elif arry[1] < I <= arry[2]:
    bonus = (I - arry[1]) * rate[2] + sum(bonu[0:2])
    print("奖金总数为:{0:.2f}".format(bonus))
elif arry[2] <= I < arry[3]:
    bonus = (I - arry[2]) * rate[3] + sum(bonu[0:3])
    print("奖金总数为:{0:.2f}".format(bonus))
elif arry[3] <= I < arry[4]:
    bonus = (I - arry[3]) * rate[4] + sum(bonu[0:4])
    print("奖金总数为:{0:.2f}".format(bonus))
elif I > arry[4]:
    bonus = (I - arry[4]) * rate[5] + sum(bonu[0:5])
    print("奖金总数为:{0:.2f}".format(bonus))
else:
    print("输入格式错误！")

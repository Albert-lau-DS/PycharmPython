# CalBMIv2.py
height, weight = eval(input("请输入身高(米)和体重\(公斤)[逗号隔开]："))
bmi = weight / pow(height, 2)
print("BMI数值为:{:.2f}".format(bmi))
who = ''
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi < 24:
    who = "正常"
elif 24 <= bmi < 28:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI指标为:国内'{0}'".format(who))

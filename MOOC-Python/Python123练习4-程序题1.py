# 身体质量指数BMI.py
# BMI ：Body Mass Index 国际上常用的衡量人体肥胖和健康程度重要标准，主要用于统计分析
# 定义：BMI = 体重 (kg) /身高2(m2)
# 获取用户输入的体重和身高值，计算并给出国际和国内的 BMI 分类
# (1) 混合计算并给出国际和国内的 BMI 分类；
# (2) 使用input()获得测试用例输入时，不要增加提示字符串。
# 输入示例1:1.68,41
# 输出示例1:
# BMI数值为:14.53
# BMI指标为:国际'偏瘦',国内'偏瘦'
# 输入示例2:1.72,80
# 输出示例2:
# BMI数值为:27.04
# BMI指标为:国际'偏胖',国内'偏胖'
height, weight = eval(input())
bmi = weight / pow(height, 2)
print("BMI数值为:{:.2f}".format(bmi))
who, nat = '', ''
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI指标为:国际'{0}',国内'{1}'".format(who, nat))


# 参考代码
height, weight = eval(input())
bmi = weight / pow(height, 2)
print("BMI数值为:{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI指标为:国际'{0}',国内'{1}'".format(who, nat))
# 这是本课程的实例5：
# (1) 多分支条件之间的覆盖是重要问题;
# (2) BMI分类：

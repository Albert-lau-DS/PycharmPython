# 百分制成绩转换五分制E.py
# 编写一个学生成绩转换程序，用户输入百分制的学生成绩，
# 成绩大于等于90且小于等于100的输出为“A”，
# 成绩大于或等于80且小于90的输出为“B”，
# 成绩大于或等于70且小于80的输出为“C”，
# 成绩大于或等于60且小于70的输出为“D”，
# 成绩小于60且大于等于0的输出为“E”，
# 如果输出的成绩大于100或小于0，输出'data error!'。
# 输入格式:输入一个数字，代表百分制成绩。
# 输出格式:A、B、C、D、E中的一个字母，表示五分制的成绩等级；或输出'data error!'
score = eval(input())
grade = 'EEEEEEDCBAA'
if score < 0 or score > 100:
    print('data error!')
else:
    print(grade[int(score//10)])

# 答案解析
score = int(input())
degree = 'AABCDEEEEEE'  # 采用正序来选择，用10-score//10来得到位置参数
# 采用条件表达式，因为只有两种选项，所以可以直接用条件表达。
print('data error!') if (score > 100 or score < 0) else print(degree[10-score//10])

# 百分制成绩转换五分制.py
# 编写一个学生成绩转换程序，用户输入百分制的学生成绩，成绩大于或等于90的输出为“A”，
# 成绩大于或等于80且小于90的输出为“B”，成绩大于或等于70且小于80的输出为“C”，
# 成绩大于或等于60且小于70的输出为“D”，成绩小于60的输出为“E”
# 输入格式:输入一个不超过100的正数，代表百分制成绩。
# 输出格式:A、B、C、D、E中的一个字母，表示五分制的成绩等级

score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')

# 答案解析
# 用户输入百分制的学生成绩，转换为五分制输出
# 常规做法， 根据分数的范围输出不同的等级
score = int(input())

if 90 <= score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >= 0:
    grade = 'E'
else:
    grade = 'data error!'
print(grade)

# 非常规做法
# score = 'EEEEEEDCBAA'
# print(score[int(input()) // 10])
# 把score做成一个字符串，然后将输入的大小除于10后取整，再以该整数去索引字符串的位置。

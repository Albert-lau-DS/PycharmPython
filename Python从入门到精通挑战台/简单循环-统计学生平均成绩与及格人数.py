# 统计学生平均成绩与及格人数.py
# 编写程序，计算学生们的平均成绩.
# 并统计及格（成绩不低于60分）的人数,题目保证输入与输出均在整型范围内。
# 在一行中给出n个非负整数，即这n位学生的成绩，其间以空格分隔。
# 按照以下格式输出：
# average = 成绩均值 count = 及格人数
score = list(map(int, input().split()))
average = sum(score) / len(score)
count = 0
for i in range(len(score)):
    if score[i] >= 60:
        count = count + 1
print("average = {}\ncount = {:.0f}".format(average, count))

## 答案解析

score = list(map(int, input().split()))
# 通过map()和list()函数把用户输入转化成int列表
average = sum(score) / len(score)
# 用总和除以数量得到平均分
count = len(list(x for x in score if x >= 60))
# 通过列表条件表达式得到大于60分的列表然后用len()函数得到数量
print("average = {}".format(average))
print("count = {}".format(count))

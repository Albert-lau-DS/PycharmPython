# 描述
# 编写一个学生成绩转换程序，用户输入百分制的学生成绩，
# 成绩大于或等于90且小于或等于100的输出为“A”，
# 成绩大于或等于80且小于90的输出为“B”，
# 成绩大于或等于70且小于80的输出为“C”，
# 成绩大于或等于60且小于70的输出为“D”，
# 成绩小于60的输出为“E”。
# 输入数据不合法时输出“data error!”。
# 用户可反复输入成绩进行转换，输入负数时输出“end”并结束程序
# 输入格式：每次输入一个浮点数，代表百分制成绩；反复输入，输入负数结束程序
# 输出格式：根据每一次的输入值分别输出A、B、C、D、E中的一个字母或"data error!"或"end"。
# 输出end时程序结束。

score = ['A', 'B', 'C', 'D', 'E', 'end', 'data error!']
while True:
    num = eval(input())
    if 90 <= num <= 100:
        print(score[0])
    elif 80 <= num < 90:
        print(score[1])
    elif 70 <= num < 80:
        print(score[2])
    elif 60 <= num < 70:
        print(score[3])
    elif 0 <= num < 60:
        print(score[4])
    elif num < 0:
        print(score[5])
        break
    else:
        print(score[6])

## 答案解析
while True:
    score = eval(input())
    if score < 0:
        print('end')
        break
    elif score > 100:
        print('data error!')
    elif score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('E')
# 索引字符串法
degree = 'EEEEEEDCBAA'
while True:
    score = float(input())
    if score < 0:
        print('end')
        break
    else:
        print('data error!') if (score > 100 or score < 0) \
            else print(degree[int(score // 10)])

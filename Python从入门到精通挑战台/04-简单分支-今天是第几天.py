# 今天是第几天.py

# 输入年/月/日（用斜杠分隔），输出该日期是这一年的第几天（题目保证年、月、日都是合法输入）？
# 输入格式:年/月/日
# 输出格式:某年某月某日是某年第多少天

# 所有时间的输入格式为xxxx/xx/xx，因此采用split('/')来分割年月日
Time = input().split('/')
year, month, day = eval(Time[0]), eval(Time[1]), eval(Time[2])
# 上述两行代码可以简化为year, month, day = map(int, input().split('/'))
# 采用map(数字类型,字符串分割状态)函数
# if eval(Time[0])%4==0 and eval(Time[0])%100!=0 or eval(Time[0])%400==0:
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Day = sum(day_month[:month - 1]) + day
print("{}年{}月{}日是{}年第{}天".format(year, month, day, year, Day))

# 答案解析
year, month, day = map(int, input().split('/'))
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days[1] = 29
sumDay = sum(days[:month - 1]) + day
print('{}年{}月{}日是{}年第{}天'.format(year, month, day, year, sumDay))

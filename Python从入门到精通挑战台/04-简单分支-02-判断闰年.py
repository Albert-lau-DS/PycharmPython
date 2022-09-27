# 判断闰年.py

# 写一个程序用于判断用户输入的年份是不是闰年，如果是输出“True”，如果不是输出“False”。
# 输入格式:输入一个代表年份的正整数
# 输出格式:“True”或“False”

# 能被400整除是闰年；能被4整除且同时不能被100整除的是闰年
# 地球绕太阳公转，大约365.25天转一圈，为了方便计算，在公历历法里，让每年的天数是整数，
# 他们规定年份能被4整除的年是闰年，这一年有366天，其他的年一年有365天。
# 但是每4年加一天这种，加的太多了，如果是几年十几年还好，如果是几千年上万年，还是有很大误差。
# 需要往回再稍微减一点，经过计算，规定，在4年一闰的基础上，能被100整除的年不是闰年
num = int(input())
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("True")
else:
    print("False")

## 答案解析
# 简易版输出格式
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(True)
else:
    print(False)

# 条件表达式：# 通过一行代码来进行判断输出是True还是False
# 格式为print(输出) if () else print(输出)
year = int(input())
print(True) if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else print(False)


#  函数
def leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        # 能被400整除是闰年；能被4整除且同时不能被100整除的是闰年
        return True
    else:
        return False


print(leap(int(input())))


def leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


print(leap(int(input())))
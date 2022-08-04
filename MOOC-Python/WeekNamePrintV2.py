# WeekNamePrintV2.py

weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字(1-7)："))
print("星期" + weekStr[weekId - 1])  # weekStr取出来的字符是字符串类型，因为可以相加

for i in range(12):
    print(chr(9800+i),end='')

# DayDayUpQ1.py

dayfactor = 0.001
daynum = 365
dayup = pow((1+dayfactor), daynum)
daydown = pow((1-dayfactor), daynum)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
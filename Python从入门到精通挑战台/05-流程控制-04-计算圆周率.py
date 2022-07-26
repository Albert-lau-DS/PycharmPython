# 描述
# 根据下面的泰勒级数关系式，依次累加绝对值不小于阈值的项，求圆周率的值。
# ![](C:/Users/80549/AppData/Local/Temp/a11e3e96ea6262da45b9b7715102.png)
# 输入格式：在一行中给出小于1且大于0的阈值。
# 输出格式：输出满足阈值条件的近似圆周率，精确到小数点后6位。

threshold = eval(input())
i, count = 0, 0
result = pow(-1, i)/(2*i+1)
while abs(result) >= threshold:
    count += result
    i += 1
    result = pow(-1, i) / (2 * i + 1)
print("{}".format(round(count*4, 6)))
# print("{:.6f}".format(pi4*4))  不要忘记这种格式"{:.6f}.format()"

# print("{}".format(round(count, 6)*4)) 不能取小数点六位后再进行乘于6的运算

## 答案解析
threshold = eval(input())
pi4 = k = 0
f = 1
while abs(1 / (2 * k + 1)) >= threshold:
    pi4 = pi4 + f * 1 / (2 * k + 1)
    k = k + 1
    f = -f
print("{:.6f}".format(pi4*4))
'''
threshold=eval(input())
item=1
pi_4=1
k=0
while abs(item)>=threshold:
    k=k+1
    item=(-1)**k/(2*k+1)
    pi_4=pi_4+item    
print("{:.6f}".format(pi_4*4))
'''





# 初步的思考是写一个函数来计算result = pow(-1, i)/(2*i+1)和累加值
# 由于没有考虑到result的值需要用来作比较，因此注释部分作废
# def Calpi(n):
#     count = 0.0
#     for i in range(1, n+1):
#         result = pow(-1, i)/(2*i+1)
#         count += result
#     result
#     return  result,count
#
#
# mini = input()
# result,count = Calpi(mini)
# while result >= result:
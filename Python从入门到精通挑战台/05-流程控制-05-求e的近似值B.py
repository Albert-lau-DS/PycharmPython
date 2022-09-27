# 描述
# 自然常数e可以用级数1+1/1!+1/2!+⋯+1/n!来近似计算。
# 本题要求用该公式计算e的近似值，若最后一项（1/n!）小于给定的阀值时，终止计算（该项不计入）。
# 输入格式：输入一个小于 1 的浮点数做为阈值
# 输出格式：输出满足阈值条件的近似 e，输出保留小数点后 8 位。

import math
threshold = eval(input())
num, count = 0, 0
single = 1/math.factorial(num)
while single >= threshold:
	count += single
	num += 1
	single = 1 / math.factorial(num)
print("{}".format(round(count, 8)))  # 这种方式相较比较复杂
# print("{:.8f}.format(count)")


## 答案解析
# 自然常数e可以用级数1+1/1!+1/2!+⋯+1/n!来近似计算。
# 本题要求用该公式计算e的近似值，直至公式里最后一项（1/n!）小于给定的阀值为止（小于给定阀值的第一项也要计入）。
# 输入格式:
# 输入一个小于1的浮点数做为阀值
# 输出格式:
# 输出满足阈值条件的近似e，输出保留小数点后八位。
# 分析：从第2项开始，每项的分母为自然数的阶乘，
# 可用math.factorial(i)或math.prod(range(1, i + 1))获得，
# 也可以用累乘的方法获得
import math
threshold = float(input())                 # 输入一个小于1的浮点数做为阀值
e = 1                                      # 取第一项作为e的初值
i = 1                                      # 分母序列的初值
while True:                                # 构建无限循环
	if 1 / math.factorial(i) < threshold:  # 设定终止条件，最后一项（1/n!）小于给定的阀值时
		break                              # 提前终止循环
	else:                                  # 最后一项（1/n!）大于或等于给定的阀值时
		e = e + 1 / math.factorial(i)      # 将当前 i 的阶乘分之一累加到e上，得到新的e值
		i = i + 1                          # 分母序列下一个数
print("{:.8f}".format(e))                  # 按要求格式输出，保留8位小数

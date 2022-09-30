# 描述
# 计算函数曲线在区间(a,b)与x轴包围的面积，可将这个区域平行于y轴切分成相等宽度的小梯形，
# 每个梯形的面积可近似求出，所有梯形面积的和就是函数曲线与x轴包围的面积，
# 也就是函数在给定区间的积分值，dx越小，梯形近似度越高，计算结果越精确，
# 也就是说区间切分段的越多，结果越精确。
# 参考下图，计算函数sin(x)在区间(a,b)与x轴包围的面积，
# a,b由用户输入，区间切分多少段也由用户输入。
# https://python123.io/images/17/87/f660515a71413f703b0e21c6b06c.png
# 输入格式：输入包括两行
# 第一行是由空格分隔的两个实数，代表积分区间(input().split()可把空格分隔的输入切分成两部分)
# 第二行是一个正整数，代表切分数量
# 输出格式：积分值，结果保留2位小数

## 出错的原因在于当成矩形来计算，其实应该采用梯形来进行计算
import math

left, right = input().split()
left, right = eval(left), eval(right)
num = int(input())
dx = (right-left)/num
count = 0.0
for i in range(1,num+1):
    x = left + dx*i
    y = abs(math.sin(x))
    s = dx*y
    count += s
if __name__ == '__main__':
    print("{:.2f}".format(count))

## 修正版
import math

left, right = input().split()
left, right = eval(left), eval(right)
num = int(input())
dx = (right-left)/num
count = 0.0
for i in range(1,num+1):
    x1 = left + dx*(i-1)
    x2 = left + dx*i
    y1 = abs(math.sin(x1))
    y2 = abs(math.sin(x2))
    s = dx*(y1+y2)/2
    count += s
if __name__ == '__main__':
    print("{:.2f}".format(count))


## 答案解析
# 梯形的上底 abs(math.sin(x + i * dx)，函数值可能为负，用abs()取其绝对值
# 梯形的下底 abs(math.sin(x + i * dx + dx)) ，函数值可能为负，用abs()取其绝对值
# 梯形的面积公式:(上底+下底)×高÷2, 用字母表示:S=(a+c)×h÷2

import math

a, b = map(float, input().split())  # 输入区间起点和终点
n = int(input())                    # 输入区间切分数量
area = 0                            # 面积初值
x = a                               # 设定起点x值
dx = abs(a - b) / n                 # 计算每个小区间的高度，即每个小梯形的高度
for i in range(n):                  # 遍历n个区间，计算每个小梯形面积并累加到一起
    area = area + dx * (abs(math.sin(x + i * dx)) + abs(math.sin(x + i * dx + dx))) / 2
print("{:.2f}".format(area))        # 输出面积值
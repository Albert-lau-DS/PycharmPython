import math

inch = 2.54
B = int(input())
S = int(input())

s_1 = pow(B * inch / 2, 2)
s_2 = pow(S * inch / 2, 2)

p = s_1 / s_2

print(math.ceil(p))

## 答案解析
import math  # 导入math模块

m = int(input())  # 输入大披萨直径 m英寸
n = int(input())  # 输入小披萨直径 n英寸

radius_of_m = int(m * 2.54) / 2  # 计算大披萨直径，厘米，取整，再计算半径
radius_of_n = int(n * 2.54) / 2  # 计算小披萨直径，厘米，取整，再计算半径
num = (radius_of_m * radius_of_m) / (radius_of_n * radius_of_n)  # 计算大小披萨面积比值
print(math.ceil(num))  # 格式化输出向上取整

# if num > int(num):
#     num = int(num) + 1
# print(int(num))

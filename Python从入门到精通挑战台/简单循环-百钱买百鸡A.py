# 百钱买百鸡A.py
# 我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何？

x_max = int(100/5)
y_max = int(100/3)
z_max = int(100/(1/3))
money = 100
for i in range(1,x_max):
    rest1 = 100 - 5*i
    for j in range(1,y_max):
        rest2 = rest1 - 3*j
        for k in range(1,z_max):
            rest3 = rest2 - 1/3*k
            if rest3 == 0 and i+j+k == 100:
                print("{} {} {}".format(i,j,k))

## 答案解析
for cock in range(1, 101):                 # 公鸡数量不为0且小于或等于100
    for hen in range(1, 101):              # 母鸡数量不为0且小于或等于100
        for chicken in range(1, 101):   # 小鸡数量大于0小于等于100且是3的倍数
            if chicken % 3 == 0:
                if cock + hen + chicken == 100 and 5 * cock + 3 * hen + chicken // 3 == 100:
                    print(cock, hen, chicken)  # 遇到满足条件的数字组合就输出
# 答案的思路是将ijk嵌套循环，只数都在一百只以内（因为题目要求在100只）
# k的数值必须是3的倍数，因为一钱就能买三只，最后列方程进行求解，解只数与钱是否都为一百

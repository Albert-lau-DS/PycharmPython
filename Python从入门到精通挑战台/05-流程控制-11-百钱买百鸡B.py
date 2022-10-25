# 描述
# 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何。
# 现在的问题是：用户输入鸡的数量和钱数，鸡翁、鸡母、鸡雏各为多少？
# 如果有解，输出全部解，并按鸡翁数量由少到多的顺序输出；如果无解则输出“无解”。
# 输入格式：用户在同一行内输入用空格分隔的两个正整数，分别表示鸡的数量和钱数
# 输出格式：每行输出一组结果，按鸡翁数、鸡母数、鸡雏数的顺序输出；
# 有多组解时，按鸡翁数量由少到多输出;如果无解则输出“无解”。

num = input().split(" ")
# print(num)
ls = []
num_c = int(num[0])
num_m = int(num[1])
a, b, c = int(num_m/5), int(num_m/3), int(num_m*3)
for i in range(1, a):
    rest2 = num_m - i*5
    for j in range(1, b):
        rest1 = rest2 - j*3
        for k in range(1, c):
            rest = rest1 - k/3
            if rest == 0 and i+j+k == num_c:
                ls.append((i, j, k))
if not ls:
    print("无解")
else:
    for p in range(len(ls)):
        print("{} {} {}".format(ls[p][0], ls[p][1], ls[p][2]))


# 答案解析
# 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何？
# 现在的问题是：用户输入钱和鸡的总数，计算鸡翁、鸡母、鸡雏各为多少？如果有解，输出全部解，并按鸡翁数量由少到多的顺序输出；如果无解则输出“无解”。
num, money = map(int, (input().split()))
flag = 0
for x in range(1, money // 5 + 1):
    for y in range(1, money // 3 + 1):
        z = num - x - y  # 鸡雏的数量等于总数减鸡翁和鸡母的数量
        if z % 3 == 0 and z > 0 and 5 * x + 3 * y + z // 3 == money:
            print(x, y, z)
            flag = 1  # 如果找到满足的解那么flag从0变为1
# 如果找不到满足的解则输出无解
if flag == 0:
    print('无解')

# 三位水仙花数.py
# "水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。
# 请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。

# 常规版
n = 1000
total = 0
for i in range(100, n):
    j = str(i)
    if eval(j[0]) ** 3 + eval(j[1]) ** 3 + eval(j[2]) ** 3 == i:
        total += i
print(total)


# 函数版
def flowers(n):
    max1 = 10 ** n
    min1 = 10 ** (n - 1)
    summary = []
    for i in range(min1, max1):
        j = str(i)
        sum1 = 0
        for k in range(len(j)):
            sum1 += eval(j[k]) ** n
            if sum1 == i:
                summary.append(i)
                break
    return summary


list_flowers = flowers(3)
print(sum(list_flowers))

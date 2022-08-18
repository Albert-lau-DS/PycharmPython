# 三位水仙花数.py
# "水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。
# 请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。

# 常规版
n = 1000
s = ''
for i in range(100, n):
    j = str(i)
    if eval(j[0]) ** 3 + eval(j[1]) ** 3 + eval(j[2]) ** 3 == i:
        s += '{},'.format(i)

print(s[:-1])


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

# 【参考代码】

s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]), 3) + pow(eval(t[1]), 3) \
            + pow(eval(t[2]), 3) == i:
        s += "{},".format(i)
print(s[:-1])
# 这里采用了s[:-1]方式不输出最后一个逗号。
# 也可以把所有结果放到一个列表中，采用字符串的.join()方法输出结果。
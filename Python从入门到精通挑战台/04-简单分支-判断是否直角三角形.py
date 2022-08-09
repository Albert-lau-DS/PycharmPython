# 判断是否直角三角形.py
# 输入三个数a,b,c, 判断能否以它们为三个边长构成直角三角形。若能，输出YES，否则输出NO。
# 输入格式:输入包括三行,每行是一个数字
# 输出格式:'YES' 或'NO'
a, b, c = eval(input()), eval(input()), eval(input())
if pow((a ** 2 + b ** 2), 0.5) == c or pow((a ** 2 + c ** 2), 0.5) == b or pow((c ** 2 + b ** 2), 0.5) == a:
    print('YES')
else:
    print('NO')
# 修正版(还需要考虑两边之和是否大于第三边，即是否能组成一个三角形的情况)
a, b, c = eval(input()), eval(input()), eval(input())
shortest = min(a, b, c)
longest = max(a, b, c)
middle = sum([a, b, c]) - shortest - longest
if shortest <= 0 or shortest + middle <= longest:
    print("NO")
elif shortest ** 2 + middle ** 2 == longest ** 2:
    print("YES")
else:
    print("NO")

# 答案解析
a = eval(input())
b = eval(input())
c = eval(input())
shortest = min(a, b, c)
longest = max(a, b, c)
middle = sum([a, b, c]) - shortest - longest
if shortest <= 0 or shortest + middle <= longest:
    print('NO')
elif shortest ** 2 + middle ** 2 == longest ** 2:
    print('YES')
else:
    print('NO')

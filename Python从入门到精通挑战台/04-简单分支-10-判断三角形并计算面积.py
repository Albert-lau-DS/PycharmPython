# 判断三角形并计算面积.py
# 输入三个数a,b,c, 判断能否以它们为三个边长构成三角形。若能，输出YES和三角形面积（结果保留2位小数），否则输出NO。
# 输入格式:输入包括三行,每行是一个数字
# 输出格式:如果输入的三个数字能够组成三角形的三边，则输出为两行，
# 分别是'YES' 和面积值（结果保留2位小数）；如果输入的三边不能组成三角形，则输出为'NO'

a, b, c = eval(input()), eval(input()), eval(input())
shortest = min([a, b, c])
longest = max([a, b, c])
middle = sum([a, b, c]) - shortest - longest
if shortest > 0 and shortest + middle > longest:
    # 因为这里是判断为可以组成三角形的，因此逻辑词必须为and
    # 采用海伦公式来计算
    p = sum([a, b, c])/2
    s = pow(p*(p-a)*(p-b)*(p-c), 0.5)
    print('YES')
    print("{:.2f}".format(s))
else:
    print('NO')
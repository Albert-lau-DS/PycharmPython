# 描述
# 《九章算术》的“盈不足篇”里有一个很有意思的老鼠打洞问题。
# 原文这么说的：今有垣厚十尺，两鼠对穿。大鼠日一尺，小鼠亦一尺。大鼠日自倍，小鼠日自半。
# 问：何日相逢？各穿几何？
# 这道题的意思就是说，有一堵十尺厚的墙，两只老鼠从两边向中间打洞。
# 大老鼠第一天打一尺，小老鼠也是一尺。
# 大老鼠每天的打洞进度是前一天的一倍，小老鼠每天的进度是前一天的一半。
# 问它们几天可以相逢，相逢时各打了多少。
# （注：本题禁止使用幂运算）
# 输入格式：
# 输入1个整数，代表墙的厚度，单位为尺
# 输出格式：
# 第一行输出1个整数，表示相遇时所需的天数
# 第二行输出2个浮点数，分别为小鼠和大鼠打洞的距离，单位为尺，保留小数点后1位数字。

# (没有头绪)
# num = 10
# rest = num
# bmouse, smouse = 1.0, 1.0
# d_b, d_s = 0.0, 0.0
# count, dot = 0.0, 0
# while rest > 0:
#     dot += 1
#     d_b += bmouse
#     d_s += smouse
#     count = d_s + d_b
#     rest = num - count
#     if rest > 0:
#         bmouse = bmouse * 2
#         smouse = smouse / 2
# print(dot)
# print(round(bmouse, 1), round(smouse, 1))

## 答案解析
n = int(input())
rat, mouse, day, time = 1, 1, 0, 1
distance_of_rat, distance_of_mouse = 0, 0  # 大老鼠和小老鼠的打洞距离
while n > 0:
    if n - mouse - rat < 0:
        time = n / (mouse + rat)
    n = n - mouse - rat
    distance_of_mouse = distance_of_mouse + time * mouse
    distance_of_rat = distance_of_rat + time * rat
    rat = rat * 2
    mouse = mouse / 2
    day = day + 1
print(day)
print(round(distance_of_mouse, 1), round(distance_of_rat, 1))
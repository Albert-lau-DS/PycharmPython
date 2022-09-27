# 出租车计费.py
# 某城市出租车计费标准如下：
# （1）起步里程为3公里(含3公里)，起步费13元；
# （2）载客里程3~15公里范围的，除起步费外，超过3公里的部分按基本单价2.3元/公里计算；
# （3）载客里程超过15公里的，15公里内的按照（2）计算，超过15公里的基本单价加收50%的费用；
# （4）时速低于12公里/小时的慢速行驶时间计入等待时间，每等待1分钟加收1元；
# 请输入乘车里程（整数）、等待时间，输出车费。
# 输入格式：在同一行输入两个正整数，分别表示行驶里程与等待时间，数字间以半角逗号分隔。
# 输出格式：输出车费，取整，保留0位小数

combo = input().split(',')
spend = 2.3
distance, waiting = eval(combo[0]), eval(combo[1])
if 0 < distance <= 3:
    cost_distance = 13
elif 3 < distance <= 15:
    cost_distance = 13 + (distance - 3) * spend
else:
    cost_distance = 13 + 12 * spend + (distance - 15) * spend * (1 + 0.5)
cost_waiting = waiting * 1
print("{:.0f}".format(int(cost_distance + cost_waiting)))

# 答案解析
distance, wait = map(int, input().split(','))
if distance <= 3:  # 如果行驶里程不超过起步里程
    fee = 13 + wait * 1  # 收费为起步价与等待费用之和
elif 3 < distance <= 15:  # 如果行驶里程超过起步里程但不超过15公里
    fee = 13 + (distance - 3) * 2.3 + wait * 1
    # 收费为起步费+超过3公里的部分2.3元/公里+等待费用
else:
    # 如果行驶里程超过15公里，15公里内的按照（2）计算，
    # 超过15公里的基本单价加收50%的费用2.3 * (1 + 0.5)
    fee = 13 + (15 - 3) * 2.3 + (distance - 15) * 2.3 * (1 + 0.5) + wait * 1
print("{:.0f}".format(fee))  # 保留0位小数

# 四位玫瑰数
# 四位玫瑰数是4位数的自幂数。自幂数是指一个 n 位数，
# 它的每个位上的数字的 n 次幂之和等于它本身。
# 例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，
# 3位数的自幂数被称为水仙花数。
# 请输出所有4位数的四位玫瑰数，按照从小到大顺序，每个数字一行。
mi = 4
nums = {}
s = 0
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                m = eval("{}{}{}{}".format(i, j, k, l))
                n = i ** mi + j ** mi + k ** mi + l ** mi
                if m == n:
                    nums[s] = m
                    s += 1
for i in range(len(nums)):
    print("{}".format(nums[i]))

# 答案解析
s = ""
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]), 4) + pow(eval(t[1]), 4) + \
       pow(eval(t[2]), 4) + pow(eval(t[3]), 4) == i:
        print(i)

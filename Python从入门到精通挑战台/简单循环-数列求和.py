# 数列求和
# 用户输入一个小于10的正整数，求1 + 12 + 123 + 1234 + …… 的前n项的和
# 输入一个正整数 n（测试数据保证小于10）
# 输出数列的和

n = int(input())
num = 0
count = 0
j = 1
k = n
count = {}
if n >= 10:
    print("测试数据保证小于10")
else:
    while j < k + 1:
        for i in range(1, n + 1):
            m = n - i
            num += i * pow(10, m)  # 不断累加
        n = n - 1
        count[j] = num  # 这里我采用了字典的方式
        j = j + 1
print(count[k])

## 答案解析

my_sum, temp = 0, 0 # 这里采用双赋值的方法，将sum和temp分别赋值为0,0
n = int(input())
for i in range(1, n + 1):
    temp = temp * 10 + i  # 每次循环使temp乘10加i
    my_sum = my_sum + temp  # 累加temp赋值给my_sum
print(my_sum)

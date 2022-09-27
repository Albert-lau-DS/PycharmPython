# 描述
# 用户输入一个小于10的正整数，求1 + 12 + 123 + 1234 + …… 的前n项的和
# 当输入大于或等于10时，输出“data error!”
# 输入格式：一个小于10的正整数
# 输出格式：数列的前 n 项和或“data error!”


# 我的解题思路是输入数字之后判断数字是否符合规范
# 首先是要大于0小于10，且不能有小数
# 其次就是写入一个函数，该函数进行计算，也就是特殊数列的求和计算
# 在该函数中，使用字符串的形式来进行逐个取数相加，不需要去乘于10
def sumsl(number):
    string = ''
    for i in range(1, number+1):
        string += str(i)
    count = 0
    for j in range(len(string)):
        count = count + eval(string[:j+1])
    return count


num = eval(input())
if num >= 10 or num <= 0:
    print('data error!')
else:
    if num != int(num):
        print('data error!')
    else:
        print(sumsl(num))


# 答案解析
n = int(input())  # 输入1-9的数字
if n <= 9:
    total = 0
    tmp = 0  # 用来存上一个数
    for i in range(1, n + 1):
        # 有点像是动态规划，将上一个数字保存下来，然后乘于10再加入下一个数字
        tmp = tmp * 10 + i  # 计算下一个要加的数: 1 —> 12，1234 —> 12345
        total = total + tmp
    print(total)
else:
    print('data error!')  # 若输入的数字不符合规定，则data error

# 面向测试用例编程
# print([1, 13, 136, 1370, 13715, 137171, 1371738, 13717416, 137174205][n - 1])
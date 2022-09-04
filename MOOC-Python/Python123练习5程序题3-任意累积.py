# 任意积累

# 请根据编程模板补充代码，计算任意个输入数字的乘积。
# 注意，仅需要在标注...的地方补充一行或多行代码。
# def getnum():
#     iNumStr = []
#     num = input()
#     while num != '':
#         iNumStr.append(num)
#         num = input()
#     return iNumStr
#
#
# def cmul(iNumStr):
#     n = len(iNumStr)
#     s = 1
#     for i in range(n+1):
#         s *= iNumStr[i]
#     return s
#
#
# s = cmul(getnum())
# print("{}".format(s))
# print(eval("cmul({})".format(input())))


# 答案解析
def cmul(a, *b):  # 同时输入所需要的数字,用逗号分隔开.
    m = a
    for i in b:
        m *= i
    return m


print(eval("cmul({})".format(input())))

# 该程序需要注意两个内容：
# 1. 无限制数量函数定义的方法，其中b在函数cmul中表达除了a之外的所有输入参数；
# 2. 以字符串形式调用函数的方法，"cmul()"与eval()的组合，提供了很多灵活性。

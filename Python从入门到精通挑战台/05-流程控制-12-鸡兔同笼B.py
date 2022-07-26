# 描述
# 一个笼子里面关了若干只鸡和兔子（鸡有2只脚，兔子有4只脚，没有例外），
# 已经知道了笼子里面脚的总数feet，则笼子里至少有多少只动物，至多有多少只动物？
# 输入格式：第一行输入一个正整数，表示测试数据的组数n
# 接下来的n行，每行一个非负整数，代表脚的数量（输入数据可能是不合理的数字）
# 输出格式：输出包含n行，每行对应一个输入，
# 包含两个正整数，第一个是最少的动物数，第二个是最多的动物数，两个正整数间用一个空格分开
# 如果没有满足要求的答案，则输出用空格分隔的两个0

## 修正版(没有头绪)
n = int(input())  # 第一行输入一个正整数，表示测试数据的组数n
for i in range(n):
    feet = int(input())  # 不断输入测试的组，总共n次
    if feet % 4 == 0:
        # 如果feet的数值可以被4整除，那么最少为整除4，最多为整除2
        least, most = feet//4, feet//2
    elif feet % 2 == 0:
        # 如果feet的数值不能被4整除，那么feet减少2再除于4。
        # 剩下的数值最少为整除4，最多为整除2
        least, most = (feet - 2)//4 + 1, feet//2  # 加1的意义在于要加上鸡的数量
    else:
        least, most = 0, 0
    print(least, most)



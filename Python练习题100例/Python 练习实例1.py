# 练习实例1.py
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去掉不满足条件的排列。
l = 0
List = {}
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and i != k and j != k:
                List[l] = eval("{}{}{}".format(nums[i], nums[j], nums[k]))
                l += 1
print(List)
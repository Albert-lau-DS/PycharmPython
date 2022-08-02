# Sequential_search1.py
a = [1, 4, 6, 32, 34, 7, 45, 9, 17, 22]
T = 9
b = sorted(a)
print(b)
# a为数组，T为目标数字
for i in range(len(b)):
    if b[i] == T:
        print("所查找的数字在数组中的第", i + 1, "位")
        break  # 当找到这个数字后直接跳出程序，不再执行。
        # 缺点在于，若数组中含有两个大小相同而位置不同的目标数字，就只能找到排在前面的数字。
    if b[i] != T and i == len(b) - 1:
        print("所查找的数字在数组中不存在")


def Sequential_search1(array, target):  # array为数组，target为目标数字
    for i in range(len(array)):
        if b[i] == target:
            print("所查找的数字在数组中的第", i + 1, "位")
            break  # 当找到这个数字后直接跳出程序，不再执行。
            # 缺点在于，若数组中含有两个大小相同而位置不同的目标数字，就只能找到排在前面的数字。
        if target > b[i]:
            print("所查找的数字在数组中不存在")
            break
        if b[i] != target and i == len(array) - 1:
            print("所查找的数字在数组中不存在")
            break


a = [1, 4, 6, 32, 34, 7, 45, 9, 17, 22]
b = sorted(a)
Sequential_search1(b, 23)


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


testList = [1, 2, 3, 4, 5, 6, 23, 34, 24, 32]
print(sequentialSearch(testList,5))


# Straight_Select_Sorting.py
A = [41, 54, 95, 32, 11, 5, 7, 10, 21, 9, 85, 12, 13, 15, 64, 84]
for i in range(len(A)):
    # a是原数组的首位，b是不断缩小的数组中的最小值，c是不断缩小的数组中的最小值的索引值
    a, b, c = A[i], min(A[i:len(A)]), A.index(min(A[i:len(A)]))
    # 将原数组的首位数字与原数组的最小值进行交换
    A[i], A[c] = b, a
print(A)
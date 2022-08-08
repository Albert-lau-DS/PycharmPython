# Insertion_Sort.py
A = [41, 54, 95, 32, 11, 5, 7, 10, 21, 9, 85, 12, 13, 15, 64, 84, 84]
# Mode 1
Mode1_B = []
for i in range(len(A)):
    Mode1_B.append(min(A))
    A.remove(min(A))
    # 使用remove函数的优势在于，如果A数组中有重复的数值，也能计算得到。
print(Mode1_B)


# Mode 2
def insertion_sort(A):
    for i in range(0, len(A)):
        index = i
        # 只要数组A的当前索引值小于前一个索引值，且当前索引位大于等于第一位。
        while A[index - 1] > A[index] and index - 1 >= 0:
            # 将当前索引位置与前一位的位置互换
            A[index], A[index - 1] = A[index - 1], A[index]
            # 互换后索引位置前移，比较该数值经历了互换位置之后，与前一个索引值的大小
            # 主要是为了判断是否需要再次互换位置
            index -= 1
    return A


A = [41, 54, 95, 32, 11, 5, 7, 10, 21, 9, 85, 12, 13, 15, 64, 84, 84]
print(insertion_sort(A))

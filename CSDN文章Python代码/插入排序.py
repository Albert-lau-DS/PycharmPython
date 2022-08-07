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

# CalpiV1.py

pi = 0
N = 100
for k in range(N):
    # 反斜杠“\”将一行代码分为几行，增加一个即可
    pi += 1 / pow(16, k) * \
          (4 / (8 * k + 1) - 2 / (8 * k + 4) -
           1 / (8 * k + 5) - 1 / (8 * k + 6))
print("圆周率值为：{}".format(pi))
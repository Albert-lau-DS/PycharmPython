# TextProBarV1.py
import time  # import后面的代码需隔一行

scale = 10
print("{0:-^16}".format("执行开始"))
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = i / scale * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    # {:^3.0f}中的:表示的是引导符
    # ^表示居中对齐，3表示的是在%之前有三个位置，.0表示的是数字为整数输出，不带小数点。
    time.sleep(0.2)
print("{0:-^16}".format("执行结束"))

# 文本进度条.py
import time

scale = 50
print("{0:-^50}".format("执行开始"))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = i / scale * 100  # 这里的100是为了转化为百分比
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.05)
print("\n{0:-^50}".format("执行结束"))

# 参考代码

import time

scale = 50
print("执行开始".center(scale // 2, '-'))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)
print("\n" + "执行结束".center(scale // 2, '-'))
# 这是本课程的实例4，请注意三点：
# (1) 文本进度条程序使用了 perf_counter() 计时，计时方法适合各类需要统间的算问题，例如：比较不同算法时间 、统计程序运行时；
# (2) 进度条的单行回退要在命令行（也叫控制台、Windows的cmd）下才能使用，IDLE屏蔽了'\r'的功能；
# (3) 进度条可应用在：任何运行时间需要较长的程序中；任何希望提高用户体验的应中；进度条是人机交互的纽带之一。

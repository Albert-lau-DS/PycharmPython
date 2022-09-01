# 递归函数实现汉诺塔

# 汉诺塔是将左侧柱子的n个圆盘移动到右侧的柱子，由于大圆盘不能放置在小圆盘上方
# 因此中间加一个过度的柱子，使移动的过程顺利进行。
count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:  # 由于只有一个圆盘，因此直接从src移动到dst即可
        print("第{}个圆盘:从{}->{}".format(1, src, dst))
        count += 1
    # 若汉诺塔的个数大于一，则需要用到中间的过渡柱子。
    # 基本思路：
    # 1. 将n-1以上的圆盘移动到中间的mid,剩下第n的圆盘在src
    # 2. 将第n个圆盘从src移动到dst
    # 3. 将n-2以上的圆盘移动到左侧的src,剩下第n-1的圆盘在mid
    # 4. 将第n-1个圆盘从mid移动到dst
    else:
        hanoi(n - 1, src, mid, dst)  # n-1以上的从左侧src出发，经右侧的dst过渡去到mid
        print("第{}个圆盘:从{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)  # n-1以上的从中间mid出发，经左侧的src过渡去到dst


hanoi(3, "A", "B", "C")
print("总共移动了{}次".format(count))

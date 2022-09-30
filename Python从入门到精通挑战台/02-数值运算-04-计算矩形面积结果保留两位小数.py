#用户输入矩形的长和宽，计算其面积，输出时精确保留2位小数。
width  = eval(input())   # 输入宽
length = eval(input())   # 输入长
print("{:.2f}".format(width*length))

## 答案解析
width = eval(input())        # 输入宽
length = eval(input())       # 输入长
area = width * length        # 计算面积
print('{:.2f}'.format(area)) # 格式化输出面积
# .2表示取小数点后2位数字，f表示浮点型

# 这里的‘{:.2f}’只采用了单引号，在输出过程中，单双引号没有本质的区别。
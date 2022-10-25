# 文本的平均列数
# 描述
# 打印输出附件文件的平均列数，计算方法如下：
# （1）有效行指包含至少一个字符的行，不计算空行；
# （2）每行的列数为其有效字符数；
# （3）平均列数为有效行的列数平均值，采用四舍五入方式取整数进位。

f = open("latex.log")
l = 0 #总行数
s = 0 #总列数
for line in f: #获取的line包含每行最后的换行符\n，所以去掉再统计
	line = line.strip("\n") #去掉line两端的换行符
	if len(line)== 0: #去掉空行
		continue
	l += 1
	s += len(line)
print(round(s/l)) #round四舍五入函数
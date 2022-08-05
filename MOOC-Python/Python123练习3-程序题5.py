# 恺撒密码.py

# 恺撒密码是古罗马恺撒大帝用来对军事情报进行加解密的算法，
# 它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，
# 即，字母表的对应关系如下：
# 原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# 对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26
# 上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26
# 假设用户可能使用的输入包含大小写字母a~zA~Z、空格和特殊符号，
# 请编写一个程序，对输入字符串进行恺撒密码加密，直接输出结果，
# 其中空格不用进行加密处理。使用input()获得输入。

# ord('a') 97
# ord('z') 122
# ord('A') 65
# ord('Z') 90
# P = input()

# for i in range(len(P)):
#     if ord('a') <= ord(P[i]) <= ord('z'):
#         C = ((ord(P[i]) - ord('a')) + 3) % 26 + ord('a')
#         P = P.replace(P[i], chr(C))
#         # 该代码块的问题出现在这里，修改P[i]不是修改了在P[i]的字母
#         # 而是修改了P里面的所有P[i]字母
#     if ord('A') <= ord(P[i]) <= ord('Z'):
#         C = ((ord(P[i]) - ord('A')) + 3) % 26 + ord('A')
#         P = P.replace(P[i], chr(C))
# print(P)

# 修正版(不能采用replace函数)
P = input()
P = list(P)
for i in range(len(P)):
    if ord('a') <= ord(P[i]) <= ord('z'):
        C = chr(((ord(P[i]) - ord('a')) + 3) % 26 + ord('a'))
        P[i] = C
    if ord('A') <= ord(P[i]) <= ord('Z'):
        C = chr(((ord(P[i]) - ord('A')) + 3) % 26 + ord('A'))
        P[i] = C
print(''.join(P))

# 参考代码
# 创建两个数组，新数组存放更改后的元素
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
    elif 'A' <= c <= 'Z':
        t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
    else:
        t += c
print(t)

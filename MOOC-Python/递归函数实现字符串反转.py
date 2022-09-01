# 递归函数实现字符串反转

def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]
        # 这里的rvs(s[1:])可以将rvs的首个字符去掉，递归不断去掉

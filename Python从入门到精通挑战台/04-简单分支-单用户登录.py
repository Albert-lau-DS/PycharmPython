# 单用户登录.py
# 简单模拟用户登陆过程，输入账户与密码，验证成功输出“Success”，失败则输出“Fail”
# 初始系统账号密码为：user="whut001" pwd="999999"
# 输入格式:分两行输入用户名和密码
# 输出格式:输出“Success”或“Fail”
username, password = input(), eval(input())
print("Success") if(username == 'whut001' and password == 999999) else print("Fail")

# 修正版(错误在于将password去掉引号了)
username, password = input(), input()
print("Success") if(username == 'whut001' and password == '999999') else print("Fail")

# 答案解析
user="whut001"
pwd="999999"

#简单登录
a=input()
b=input()
if a==user and b==pwd:
    print("Success")
else:
    print("Fail")
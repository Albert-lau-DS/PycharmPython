# 用户登录A.py
# 实现用户输入用户名和密码，当用户名为 admin且密码为123456时，显示“登录成功”，否则显示“登录失败”。
# 输入格式:用户在两行里分别输入用户名和密码
# 输出格式:"登录成功"或"登录失败"

Name, key = input(), eval(input())
print("登录成功") if Name == 'admin' and key == 123456 else print("登录失败")

# 答案解析
username = input()
password = input()
if username == 'admin' and password == '123456':
    print("登录成功")
else:
    print("登录失败")
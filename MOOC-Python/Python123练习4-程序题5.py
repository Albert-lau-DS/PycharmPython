# 用户登录的三次机会.py

# 给用户三次输入用户名和密码的机会，要求如下：
# 1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，
# 输出‘登录成功！’，退出程序；
# 2）当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。
chance = 3
username = 'Kate'
password = '666666'
while chance > 0:
    name = input()
    word = input()
    if name == username and word == password:
        print('登录成功！')
        break
    else:
        chance -= 1
else:
    print('3次用户名或者密码均有误！退出程序。')
# 这里采用for in + else 的循环高级用法
# 由于while也是循环，因此也尝试了while + else的用法
# 采用了break函数来忽略掉最后的else的部分

# 【参考答案】
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count += 1
        if count == 3:
            print("3次用户名或者密码均有误！退出程序。")
# 这里是参考答案，运用while进行非确定次数循环。

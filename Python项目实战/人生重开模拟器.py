# 人生重开模拟器

import random
import sys
import time

print("***************************************************")
print('*                                                 *')
print('*             《人生模拟重启器》——Python版            *')
print('*                                                 *')
print('*                                                 *')
print('*                                                 *')
print("***************************************************")

# 1. 设置角色初始属性
# 颜值、体质、智力、家境,这几项属性点数总和不能超过设定的阈值（这里我们设置为20）, 每一项取值都是 1-10 之间

# 使用循环, 使玩家在输入错误的时候, 可以重新输入.
while True:
    # 尽管是while True，但不一定是死循环，可以在代码块里使用break跳出整个循环
    print("请设置初始属性(可用属性点总数为 20)")
    face = int(input("请输入颜值属性点数(1-10):"))
    strong = int(input("请输入体质属性点数(1-10):"))
    iq = int(input("请输入智力属性点数(1-10):"))
    home = int(input("请输入家境属性点数(1-10):"))

    # 通过使用条件语句, 对于玩家输入的属性值做出校验检查
    # 以下这段逻辑, 也可以使用elif:使用 elif 则是多个分支只能进一个, 一旦某个条件满足了, 就不会再走其他的分支了.
    # 这里虽然没有使用 elif , 但是使用了 continue, 一旦某个条件满足, continue 就会跳出本次循环, 后续的条件判定不再执行
    if face < 1 or face > 10:
        print("颜值属性点数设置有误!")
        continue
    if strong < 1 or strong > 10:
        print("体质属性点数设置有误!")
        continue
    if iq < 1 or iq > 10:
        print("智力属性点数设置有误!")
        continue
    if home < 1 or home > 10:
        print("家境属性点数设置有误!")
        continue
    if face + strong + iq + home > 40:  # 如果当前的条件都没有被触发, 则认为玩家输入的数据是合法的.
        print("属性点数设置错误！属性点数之和超出阈值(20)")
        continue

    # 此时就可以跳出循环结束输入了
    print("初始属性设置完成!")
    print(f"颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}")
    break

# 2.设置生成角色的性别
# 使用 random.randint(beg, end), 就能生成 [beg, end] 随机整数

point = random.randint(1, 6)
# 此处的random是python中的一个模块! 相当于C++中的STL（封装好的代码块，我们直接使用即可！）
# 这里使用其他模块，需要先使用import语句，把模块的名字“导入”进来，pycharm有自动导入的功能
# print(f'point = {point}')
if point % 2 == 1:
    gender = 'boy'
    print('你出生了，是个男孩。')
else:
    gender = 'girl'
    print('你出生了，是个女孩。')

# 3.设置角色的出生环境及背景
# 为了简单方便, 这里我们就直接生成 1-3 的随机数进行模拟
# 这里我们将角色的家庭背景及环境设置四个档位梯度，不同档位会对属性有加成或减低
point = random.randint(1, 3)
if home == 10:
    # 第一档
    print('你出生在首都, 你的父母是高官政要')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    # 第二档
    if point == 1:
        print('你出生在大城市, 父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在大城市, 父母是企业高管')
        home += 2
    else:
        print('你出生在大城市, 父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    # 第三档
    if point == 1:
        print('你出生在县城, 你的父母是医生')
        strong += 1
    elif point == 2:
        print('你出生在乡镇, 你的父母是老师')
        iq += 1
    else:
        print('你出生在乡镇, 你的父母是个体户')
        home += 1
else:
    # 第四档
    if point == 1:
        print('你出生在农村, 你的父母是辛苦劳作的农民')
        strong += 1
        face -= 2
    elif point == 2:
        print('你出生在农村, 你的父母奔波劳碌，家庭状况不是很好')
        home -= 1
    else:
        print('你出生在穷乡僻壤, 你的父母艰辛茹苦，抚养你长大')
        strong -= 1
print(f'颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}')

# 4.童年阶段
for age in range(1, 11):
    # 把一整年的打印都整理到一个字符串中, 在这一年的结尾统一打印
    info = f'你今年 {age} 岁. '
    # 生成一个 [1, 3] 的随机整数.
    point = random.randint(1, 3)
    # 接下来编写各种事件的代码
    # 性别触发的事件
    if gender == 'girl' and home <= 3 and point == 1:
        info += '你的家庭封建思想重男轻女，你不幸被遗弃!'
        print(info)
        print('游戏结束!')
        sys.exit(0)
        # sys也是python中提供的一个模块，直接使用即可
    # 体质触发的事件
    # 使用 elif 是为了保证每年只触发一个事件!
    elif strong < 6 and point < 3:
        info += '你患了一场大病'
        if home >= 5:
            info += '在父母的悉心照料下, 你康复了'
            strong += 1
            home -= 1
        else:
            info += '你的父母无法照料你, 你的身体每况愈下'
            strong -= 1
    # 颜值触发的事件
    elif face <= 4 and age >= 7:
        info += '你由于很丑, 其他小朋友不喜欢你. '
        if iq > 5:
            info += '你决定通过学习提升自己!'
            iq += 1
        else:
            if gender == 'boy':
                info += '你和别的小朋友经常打架!'
                strong += 1
                iq -= 1
            else:
                info += '你经常被别的小朋友欺负!'
                strong -= 1
    # 智商触发的事件
    elif iq < 5:
        info += '你有点呆呆的 '
        if home >= 8 and age >= 6:
            info += '你的父母把你送到更好的学校学习'
            iq += 1
        elif 4 <= home <= 7:
            if gender == 'boy':
                info += '你有运动天赋，立志成为运动员'
                strong += 1
            else:
                info += '你学会了提升外在形象'
                face += 1
        else:
            # 家境 < 4
            info += '你虽然出身条件不好，但却有快乐的童年'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
            else:
                pass
    # 健康成长事件
    else:
        info += '你一生健康，没有患过大病 '
        if point == 1:
            info += '你的身体很强壮'
            strong += 1
        elif point == 2:
            info += '你的自身条件不断提升'
            face += 1
        else:
            # 无事发生
            pass

    # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}')
    print('------------------------------------------------------')
    # 为了方便观察, 加一个小小的暂停操作
    time.sleep(1)

# 5.青年阶段
for age in range(11, 20):
    info = f'你今年{age}岁.'
    point = random.randint(1, 3)
    # 性别触发的事件
    if gender == 'boy' and home <= 3 and point == 1:
        info += '你爱而不得，你喜欢的人很讨厌你...'

    # 体质触发的事件
    elif strong > 6 and point < 3:
        info += '你参加省级运动会，并获得了金牌'
        if home >= 5:
            info += '你被以"体育特长生"的名义保送到顶尖大学深造'
            home += 1
            strong += 1
        else:
            info += '你的体育天赋被埋没...'
            home -= 2
            face -= 1
    # 颜值触发的事件
    elif face >= 5 and home >= 7:
        info += '你被许多人喜欢，如众星捧月'
        if iq > 5:
            info += '你颜值、家境、才华并存，人生顺利平坦'
            home += 1
        else:
            info += '你出身条件好，但却不能自立自强'
            iq -= 2
    # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}')
    print('------------------------------------------------------')
    # 为了方便观察, 加一个小小的暂停操作
    time.sleep(1)
# 6.壮年阶段
for age in range(20, 50):
    info = f'你今年{age}岁.'
    point = random.randint(1, 3)
    # 性别触发的事件
    if gender == 'boy' and iq > 7:
        info += '你事业有成，家庭和睦'
        home += 2
        face += 1
    else:
        if home <= 3:
            info += '你自立自强，不接受命运安排'
            home += 2
            strong += 2
        else:
            info += '你平庸一生...'
    # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}')
    print('------------------------------------------------------')
    # 为了方便观察, 加一个小小的暂停操作
    time.sleep(1)
# 7.老年阶段
for age in range(50, 110):
    info = f'你今年{age}岁.'
    point = random.randint(1, 3)
    # 性别触发的事件
    if gender == 'girl' and home >= 6:
        info += '你子孙满堂，晚年享福'
        home += 1
        strong += 1
    # 体质触发的事件
    elif strong > 5 and iq > 6:
        info += '你是工作单位骨干，领导成员攻坚克难'
        if face >= 5:
            info += '你被应邀担任单位发言人'
            home += 2
        else:
            # Do Nothing!
            pass
    # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}')
    print('------------------------------------------------------')
    # 为了方便观察, 加一个小小的暂停操作
    time.sleep(1)

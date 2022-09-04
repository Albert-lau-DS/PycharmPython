# CalThreeKingdomsV2.py

import jieba

txt = open("三国演义.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
# 丞相这个词不能删除，因为在后续的分析中需要用到
excludes = {'将军', '却说', '二人', '不可', '荆州', '不能', '如此'}
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

# 进行迭代计算的时候可以将excludes及后面的for循环做一个函数来添加不符合的条件

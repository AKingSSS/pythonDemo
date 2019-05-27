"""
实例001：数字组合
题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析 遍历全部可能，把有重复的剃掉。
"""
# 我的方案①
list = [1, 2, 3, 4]
num = 0
for i in list:
    for j in list:
        if j != i:
            for k in list:
                if k != j and k != i:
                    print('三位数：', str(i) + str(j) + str(k))
                    num += 1
print('能组成' + str(num) + '个互不相同且无重复数字的三位数')

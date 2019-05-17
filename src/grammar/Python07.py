# 元组
"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
"""
from typing import List

print("# 元组")
tuple1 = ('python', 'go', 2019, 5.17)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = 'a', 'b', 'c', 'd'  # 不需要括号也可以
print(type(tuple3))
# 创建空元组
t = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
t1 = (50)
print(type(t1))  # --->> <class 'int'>
t2 = (30,)
print(type(t2))  # --->> <class 'tuple'>

# 1.访问元组
'''
元组可以使用下标索引来访问元组中的值，如下实例
'''
print("# 1.访问元组")
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1[0])
print(tup2[0:2])

# 2.修改元组
'''
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
'''
print('# 2.修改元组')
tup3 = (12, 32, 43)
tup4 = ('a', 'b', 'v')
# 创建一个新的元组
tup5 = tup3 + tup4
print(tup5)
# 以下修改元组元素操作是非法的。
'''
tup3[0] = 10
print(tup3)
TypeError: 'tuple' object does not support item assignment
'''

# 3.删除元组
'''
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
'''
print('# 3.删除元组')
tup6 = ['qq', 'wx', 'wb']
print(tup6)
del tup6
# print(tup6) ---> NameError: name 'tup' is not defined

# 4.元组运算符
print('# 4.元组运算符')
tup7 = (1, 2, 3, 4, 5)
print(len(tup7))  # 计算元素个数
tup8 = (6, 8, 9)
print(tup7 + tup8)  # 连接
print(tup8 * 2)  # 复制
print(6 in tup8)  # 元素是否存在
# 迭代
for x in tup8:
    print(x)

# 5.元组索引，截取
print("# 5.元组索引，截取")
L = ('Google', 'TaoBao', 'Runoob')
print(L[0])
print(L[-2])
print(L[1:])

# 6.元组内置函数
print("# 6.元组内置函数")
L1 = ('1', '2', '3')
print(len(L1))  # 计算元组元素的个数
print(max(L1))
print(min(L1))
'''
注意：当使用max或者min时，元组内的元素类型必须一致，否则报错
'''
oList = ['a', 'b', 'c']
nTup = tuple(oList)
print(nTup)  # 将列表转换为元组

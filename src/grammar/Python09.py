# 集合
"""
集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
param = {value01,value02,...}
或者
set(value)
"""
fruit = {'apple', 'orange', 'banana', 'apple'}
print(fruit)  # --->> {'orange', 'apple', 'banana'}
print('apple' in fruit)
a = set('abracadabra')
b = set('abc0')
print(a - b)  # 集合中包含而集合b中不包含的元素 --->> {'d', 'r'}
print(a | b)  # 集合a或b中包含的所有元素 --->> {'c', 'a', 'd', '0', 'b', 'r'}
print(a & b)  # 集合a和b中都包含了的元素 --->> {'a', 'b', 'c'}
print(a ^ b)  # 不同时包含于a和b的元素 --->> {'d', '0', 'r'}

# 1.添加元素
'''
将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
'''
print("# 1.添加元素")
s1 = {'a', 'b', 'c'}
s1.add('b')
print(s1)
s1.add('d')
print(s1)
'''
还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
s.update( x )
x 可以有多个，用逗号分开。
'''
s2 = set(("Google", "Runoob", "TaoBao"))
s2.update({1, 3})  # --->>{1, 'Google', 3, 'Runoob', 'TaoBao'}
print(s2)
s2.update([2, 4], [5, 8])
print(s2)

# 2.移除元素
'''
语法格式如下：
s.remove( x )
将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

s.discard( x )
如果元素不存在，不会发生错误

设置随机删除集合中的一个元素，语法格式如下
s.pop() 
'''
print("# 2.移除元素")
s3 = {'a', 'b', 'c'}
s3.remove('a')
print(s3)
# s3.remove('d') # 报错
s3.discard('d')  # 不报错
s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s5 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
x1 = s4.pop()
print(x1)
x2 = s5.pop()
print(x2)

# 3.计算集合元素个数
print("# 3.计算集合元素个数")
print(len(s5))

# 4.清空集合
'''
s.clear()
'''
print("s.clear()")
thisSet = set(("Google", "Runoob", "TaoBao"))
thisSet.clear()
print(len(thisSet))

# 5.判断元素是否在集合中存在
'''
x in s
'''
print("# 5.判断元素是否在集合中存在")
s6 = set(("Google", "Runoob", "TaoBao"))
print("Google" in s6)

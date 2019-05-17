# 字典
"""
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""
# 1.访问字典里的值
print("# 1.访问字典里的值")
d1 = {'name': 'python', 'age': 2}
print("d1['name']: ", d1['name'])
print("d1['age']: ", d1['age'])

# 2.修改字典
'''
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例
'''
print("# 2.修改字典")
d1['age'] = 3  # 修改信息
print("d1['age']: ", d1['age'])
d1['sex'] = 'man'  # 添加信息
print(d1)

# 3.删除字典
'''
能删单一的元素也能清空字典，清空只需一项操作。

显示删除一个字典用del命令
'''
print("# 3.删除字典")
d2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
d3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del d2['Name']
print(d2)  # --->> {'Age': 7, 'Class': 'First'}
d2.clear()  # 清空字典
print(len(d2))  # 不报错
del d3
# print(len(d3)) # NameError: name 'd3' is not defined

# 4.字典键的特性
'''
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
print("# 4.字典键的特性")
d4 = {'name': 'king', 'age': '26', 'name': 'aKing'}
print(d4)  # --->> {'name': 'aKing', 'age': '26'}
# d5 = {[1, 2]: 'king'}     # TypeError: unhashable type: 'list'

# 5.内置函数和方法
d6 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(d6))  # 计算字典元素个数，即键的总数
print(d6, type(d6))
s = str(d6)
print(s, type(s))  # 输出字典，以可打印的字符串表示


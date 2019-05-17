# 列表
# 1、创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
list1 = ['java', 'php', 'python']
list2 = [1, 2, 3, 4]
list3 = ["a", "b", "c"]
print(list1, list2, list3)

# 2、访问列表中的值
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
print('list1[0]: ' + list1[0])
# print('list1[1:2]: ' + list1[1:2])  TypeError: can only concatenate str (not "list") to str
print('list1[1:2]', list1[1:2])

# 3.更新列表
print('list2[2]: ', list2[2])
# 更新
list2[2] = 'd'
print('list2[2]: ' + list2[2])

# 4.删除列表元素
# 删除第3个元素
del list3[2]
print('list3', list3)

# 5.list的方法
# 5.1 List append()方法
'''
append() 方法用于在列表末尾添加新的对象。
append()方法语法：
list.append(obj)
'''
print("# 5.1 List append()方法")
aList = ['java', 'php']
aList.append("python")
print(aList)

# 5.2 List count()方法
'''
count() 方法用于统计某个元素在列表中出现的次数。
count()方法语法：

list.count(obj)
'''
print('# 5.2 List count()方法')
cList = ['lining', 'adidas', 'nike', 'nike']
print(cList.count('nike'))

# 5.3 List reverse()方法
'''
reverse() 函数用于反向列表中元素。
reverse()方法语法：

list.reverse()
'''
print('# 5.3 List reverse()方法')
rList = ['win10', 'win7', 'xp']
rList.reverse()
print(rList)

# 5.4 List remove()方法
print('# 5.4 List remove()方法')
mList = ['mac', 'windows', 'linux']
mList.remove('linux')
print(mList)



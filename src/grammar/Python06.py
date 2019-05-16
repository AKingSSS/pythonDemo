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

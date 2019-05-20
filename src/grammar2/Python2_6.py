# 数据结构
# 1.列表
"""
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，
一句话概括即：
列表可以修改，而字符串和元组不能。
"""
# list.append(x) ：把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
myList = [1, 2, 3]
myList.append(4)
print('myList', myList)

# list.extend(L):通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
# L可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
myList1 = [1, 2, 3]
newList = [4, 5, 6]
# myList1.append(newList)  # --->> myList1 [1, 2, 3, [4, 5, 6]]
myList1.extend(newList)  # --->> myList1 [1, 2, 3, 4, 5, 6]
print('myList1', myList1)

# list.insert(i, x)	:在指定位置插入一个元素
list1 = ['BaiDu', 'Ali', 'Tencent']
list1.insert(3, 'HuaWei')
print('list1 = ', list1)

# list.remove(x):删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误
list2 = ['php', 'java', 'python', 'net', 'java']
list2.remove('java')
print('list2 = ', list2)  # --->> list2 =  ['php', 'python', 'net', 'java']

# list.pop([i]):
# 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除
list3 = ['c', 'c++', 'java', '.net', 'python']
list3.pop(0)
print('list3 = ', list3)
list3.pop()
print('list3 = ', list3)

# list.clear()
list4 = ['cctv1', 'cctv2', 'cctv3']
list4.clear()
print('list4 = ', list4)  # --->> list4 =  []

# list.index(x)
# 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list5 = ['cctv1', 'cctv2', 'cctv3']
# print('索引 = ', list5.index('cctv5'))  # --->> 'cctv5' is not in list
print('索引 = ', list5.index('cctv2'))

# list.count(x):返回 x 在列表中出现的次数
list6 = ['cctv1', 'cctv2', 'cctv3', 'cctv2']
print('cctv2在列表出现的次数 ：', list6.count('cctv2'))

# list.sort()
list7 = ['cctv1', 'cctv2', 'cctv3', 'cctv2']
print('排序前：', list7)
list7.sort()
print('排序后：', list7)

# list.reverse() :倒排列表中的元素。
list8 = ['h', 'e', 'l', 'l', 'o']
print('倒序前：', list8)
list8.reverse()
print('倒序后：', list8)

# list.copy() ： 返回列表的浅复制，等于a[:]
list9 = ['h', 'a', 'p', 'p', 'y']
list10 = list9.copy()
print('list10 = ', list10)

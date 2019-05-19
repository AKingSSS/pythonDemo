# 循环语句
"""
Python中的循环语句有 for 和 while。
"""

# 1.while循环
'''
while 判断条件：
语句
'''
# while 来计算 1 到 100 的总和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print('sum = ', sum)

# 无限循环
'''
我们可以通过设置条件表达式永远不为 false 来实现无限循环

while True:
    num = int(input('请输入一个数字：'))
    print('你输入的数字：', num)
print('Good Bye')
'''

# while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块
count = 0
while count < 5:
    print(count, '小于5')
    count += 1
else:
    print(count, '大于或等于5')

# 简单语句组
'''
如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
'''
while False: print('hello world')

# for语句
'''
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
'''
subjects = ['python', 'java', 'php']
for sub in subjects:
    print(sub)
else:
    print("other")

'''
for 实例中使用了 break 语句，break 语句用于跳出当前循环体
'''

for sub in subjects:
    if 'java' == sub:
        print('科目：', sub)
        break
        print('######')
else:
    print('没有循环数据')
print('完成循环')

# range()函数
'''
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
ange指定区间的值
range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
结合range()和len()函数以遍历一个序列的索引
使用range()函数来创建一个列表
range(5) ------>> 0 1 2 3 4 5
range(5,8) ------>> 5 6 7
'''
for i in range(5):
    print("i = ", i)
    print('')

for j in range(5, 8):
    print("j = ", j)
    print('')

for k in range(0, 10, 2):
    print("k = ", k)
    print('')

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

rList = list(range(5))
print('rList = ', rList)
print('')

# break和continue语句及循环中的else子句
'''
break 语句可以跳出 for 和 while 的循环体。
如果你从 for 或 while 循环中终止，
任何对应的循环 else 块将不执行。 

循环语句可以有 else 子句，
它在穷尽列表(以for循环)或条件变为 false (以while循环)
导致循环终止时被执行,但循环被break终止时不执行。
'''
# break
for letter in 'python':
    if letter == 't':
        break
    print('letter: ', letter)
else:
    print('执行else下的代码')

# continue
'''
continue语句被用来告诉Python
跳过当前循环块中的剩余语句，
然后继续进行下一轮循环
'''
for letter in 'python':
    if letter == 't':
        continue
    print('letter: ', letter)

# pass语句
'''
Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句
'''
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

# 字符串
"""
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。
"""
var1 = 'hello world!'
var2 = "Python"

# 1.访问字符串中的值
'''
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

Python 访问子字符串，可以使用方括号来截取字符串
'''
print("var1[0]: " + var1[0])
print("var2[2: 5]: " + var2[2: 5])

# 2.字符串更新
# [:end] 从开头提取到end - 1
print("var1[:6]: " + var1[:6])
print(len(var1[:6]))
print("已更新字符串 : ", var1[:6] + 'Runoob!')

# 3.字符串格式化
'''
 %s	 格式化字符串
 %d	 格式化整数
'''
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
print("我的昨日收益%.2f元" % (1.53 * 2))

# 4.format 格式化函数(******需要多练******)
# 不设置指定位置，按默认顺序
print('{},{}'.format('hello', 'world '))
# 设置指定位置(位置从0开始)
print('{0},{1}'.format('hello', 'world '))
# 设置指定位置
print('{1},{0},{1}'.format('hello', 'world '))
# 设置参数
print('我叫{name},今年{age}岁！'.format(name='小新', age=10))
# 通过字典设置参数
'''
单星号是无法读取到字典中的值的，永远只会读取到字典中的键（key），
如果想读取到字典中的值，需要使用双星号(**)
后续再研究
'''
content = {'name': '小新', 'age': '10'}
print('我叫{name},今年{age}岁！'.format(**content))
# 通过列表索引设置参数
myList = ['华为', '小米', 'vivo', 'oppo']
print('国产手机品牌：{0[0]},{0[1]},{0[2]},{0[3]}'.format(myList))  # "0" 是必须的

# 数字格式化
'''
错误写法：
①没有带上引号
print({:.2f}.format('3.1415926'))
②格式化的是数字类型
print('{:.2f}'.format('3.1415926'))
'''
# 保留小数点后两位
print('{:.2f}'.format(3.1415926))
print('{:.2f}'.format(3))
# 带符号保留小数点后两位，会自动四舍五入
print('{:+.2f}'.format(3.1415926))
print('{:+.2f}'.format(3.689))  # --->> +3.69
print('{:+.2f}'.format(-2.789))  # --->> -2.79
# 不带小数
print('{:.0f}'.format(3.68))  # --->> 4
print('{:f}'.format(3.68))  # --->> 3.680000
# 数字补零 (填充左边, 宽度为2) 使用场景 日期
print('{:0>2d}'.format(5))  # 数字补零 (填充左边, 宽度为2)
print('{:x<4d}'.format(5))  # 数字补x (填充右边, 宽度为4)
# 以逗号分隔的数字格式
print('{:,}'.format(10000000))
# 百分比格式
print('{:.2%}'.format(0.25))

# 5.内置函数find
'''
Python find() 方法检测字符串中是否包含子字符串 str ，
如果指定 beg（开始） 和 end（结束） 范围，
则检查是否包含在指定范围内，
如果包含子字符串返回开始的索引值，否则返回-1。
'''

# str1 = "this is string example....wow!!!"
str1 = "the python language is a cross platform language"
str2 = "language"
print(str1.find(str2))  # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：11
print(str1.find(str2, 10))  # 从下标10开始，查找在字符串里第一个出现的子串，返回结果：11
print(str1.find(str2, 30))  # 从下标20开始，查找在字符串里第一个出现的子串，返回结果：40



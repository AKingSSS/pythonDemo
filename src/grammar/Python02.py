# 基本数据类型
"""
pyhton中的变量不需要申明。每个变量在申明前必须赋值，赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值
"""
print("# 基本数据类型")
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "python"  # 字符串
print(counter)
print(miles)
print(name)
# 1.1为多个变量赋值
print("# 1.1为多个变量赋予相同的数值")
a = b = c = 1
print(a)
print(b)
print(c)
print("# 1.1为多个变量赋予不同的数值")
e, f, g = 1, 2, "google"
print(e)
print(f)
print(g)
print(e, f, g)
# 1.2标准数据类型
'''
6个标准数据类型
不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3个）：   List（列表）、Dictionary（字典）、Set（集合）。
'''
# 1.2.1 Number（数字）
'''
Python3 支持 int、float、bool、complex（复数）
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

①内置的 type() 函数可以用来查询变量所指的对象类型。
②此外还可以用 isinstance 来判断：
'''
print("1.2.1 Number（数字）")
i, j, k, h = 100, 1000.2, True, 1 + 4j
print(type(i), type(j), type(k), type(h))
print(isinstance(i, int))
print(isinstance(j, float))
print(isinstance(k, bool))
print(isinstance(h, complex))
'''
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
    ps：后续再讲
'''

'''
注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
到 Python3 中，把 True 和 False 定义成关键字了，
但它们的值还是 1 和 0，它们可以和数字相加
'''
flag1 = True
flag2 = False
print(flag1+flag2)

'''
当你指定一个值时，Number 对象就会被创建
您也可以使用del语句删除一些对象引用，删除引用后不能被打印
del var1[,var2[,var3[....,varN]]]
'''
var1 = 1
var2 = 2
var3 = 2
print(var1, var2, var3)
del var1
# print(var1, var2, var3)
print(var2, var3)
# del var2, var3
# print(var1, var2, var3) NameError: name 'var1' is not defined

# 数值运算
print(1 + 2)        # 加法
print(1 - 2)        # 减法
print(1 * 2)        # 乘法
print(1 / 2)        # 除法，得到一个浮点数
print(1 // 2)       # 除法，得到一个整数
print(1 % 2)        # 取余
print(2 ** 3)       # 乘方  --->> 8
print(1.9 + 2.01)   # --->> 3.9099999999999997
'''
注意：
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数
'''
# 1.2.2 String（字符串）
'''
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 '\' 转义特殊字符。
字符串的截取的语法格式如下
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
'''
print("# 1.2.2 String（字符串）")
str1 = "terminal"
print(str1[6: 7])
print(str1[-2: -1])
print(str1[-1])
print(str1[-2:])

# 1.2.3 List（列表）
'''
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，
字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
'''

bigList = ['abc', 2, True, 4.5]
tinyList = ['bcd', 1]
print(bigList)          # --->['abc', 2, True, 4.5]
print(bigList[0])       # ---> abc
print(bigList[0:2])     # ---> ['abc', 2]
print(bigList[1:])      # ---> [2, True, 4.5]
print(bigList * 2)      # ---> ['abc', 2, True, 4.5, 'abc', 2, True, 4.5] 输出两次列表
print(bigList + tinyList)  # ---> ['abc', 2, True, 4.5, 'bcd', 1]  连接列表
'''
与Python字符串不一样的是，列表中的元素是可以改变的
'''
bigList[0] = "ab"
bigList[2:] = []
print(bigList)
'''
注意：

1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的

Python 列表截取可以接收第三个参数，参数作用是截取的步长，
以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串
'''
letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']

print(letters[0: -1: 2])
# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
# 翻转字符串
# 假设列表 list = [1,2,3,4],
# list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
# inputWords[-1::-1] 有三个参数
# 第一个参数 -1 表示最后一个元素
# 第二个参数为空，表示移动到列表末尾
# 第三个参数为步长，-1 表示逆向
print(letters[-1::-1])

# 1.2.4 Tuple （元组）
'''
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同
'''
print("# 1.2.4 Tuple （元组）")
t1 = ('qwe', 1, 1.02, True)
t2 = ('abc', 23)
print(t1, t2)
print(t1[0])
print(t1[0: 2])
print(t1[1:])
print(t1 * 2)       # 输出两次元组
print(t1 + t2)      # 连接元组

'''
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。
也可以进行截取（看上面，这里不再赘述）。
其实，可以把字符串看作一种特殊的元组。
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

注意：

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''

# 1.2.5 set （集合）
'''
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，
因为 { } 是用来创建一个空字典。
创建格式：
param = {value01,value02,...}
或者
set(value)
无序不重复
'''
print("# 1.2.5 set （集合）")
student = {'tom', 'ming', 'jack', 'tom', 'linda'}
print(student)          # 输出集合，重复的元素被自动去掉
# 成员测试
if 'tom' in student:
    print("tom在集合里")
else:
    print("tom不在集合里")

# 集合运算
s1 = set('adidas')
s2 = set('abc')
print(s1)
print(s1 - s2)      # 差集
print(s1 | s2)      # 并集
print(s1 & s2)      # 交集
print(s1 ^ s2)      # s1与s2中不同时存在的元素

# 1.2.6 set （字典）
'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：
字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''
print("# 1.2.6 set （字典）")
dic = dict()
dic["name"] = "python"
dic["age"] = "18"
dic[0] = '男'
tinyDic = {"name": "java", "code": 5, "site": "简书"}
print(tinyDic)
print(tinyDic['name'])
print(tinyDic.keys())
print(tinyDic.values())

dictMerged2 = dic.copy()
dictMerged2.update(tinyDic)
print(dictMerged2)

# 1.2.7 数据类型转换
# 将x转换为一个整数
word1 = '1'
word2 = '2'
print('# 1.2.7 数据类型转换')
print(int(word1) + int(word2))
# 将对象 x 转换为字符串
num1 = 12
num2 = 21
print(str(num1) + str(num2))



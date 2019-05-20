# 函数
"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
函数内容以冒号起始，并且缩进
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
"""
# 语法
'''
Python 定义函数使用 def 关键字，一般格式如下
def 函数名（参数列表）:
    函数体
'''


# 计算圆的面积
def area(r):
    s = 3.14 * (r ** 2)
    return '{:.2f}'.format(s)


print("半径为4的圆的面积：", area(4))

# 1、python 函数的参数传递
'''
①不可变类型：整数、字符串、元组
    如fun（a），传递的只是a的值，没有影响a对象本身。
    比如在 fun（a）内部修改 a 的值，
    只是修改另一个复制的对象，不会影响 a 本身。
②可变类型：列表，字典，集合
    如 fun（la），则是将 la 真正的传过去，
    修改后fun外部的la也会受影响
'''
# 1.1传不可变对象实例
'''
实例中有 int 对象 2，指向它的变量是 b，
在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，
a 和 b 都指向了同一个 Int 对象，在 a=10 时，
则新生成一个 int 值对象 10，并让 a 指向它
'''


def changeInt(a):
    a = 10


b = 2
changeInt(b)
print(b)  # --->> 2


# 1.2 传可变对象实例
def changeList(myList):
    myList.append([1, 2, 3])
    print('函数内取值：', myList)
    return


myList = [10, 20, 30]
changeList(myList)
print('函数外取值：', myList)

# 2.参数
'''
必需参数：
        必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
关键字参数：
        用于函数调用，通过“键-值”形式加以指定。
        可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
默认参数：
        调用函数时，如果没有传递参数，则会使用默认参数
不定长参数：
        处理比当初声明时更多的参数
'''


# 2.1 关键字参数
# 求长方形面积
def area(width, length):
    s = width * length
    print(s)


width = 10
length = 20
'''
以下2种写法，结果一致
'''
area(width=10, length=20)
area(length=20, width=10)

# 2.2 默认参数
'''
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
'''


def printInfo(name, age=18):
    print('名字：', name)
    print('年龄：', age)


printInfo(age=50, name='tom')
print('----------------------')
printInfo(name='john')

# 2.3不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
和上述 2 种参数不同，声明时不会命名
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
'''


def printArg(arg1, *varTuple):
    print("输出：")
    print(arg1)
    for var in varTuple:
        print(var)


printArg(10, 20, 30, 40)
print("不向函数传递未命名的变量：")
printArg(10)
'''
还有一种就是参数带两个星号 **基本语法如下
def functionName([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了两个星号 ** 的参数会以字典的形式导入
'''


def printDic(arg1, **var_args_dict):
    print("输出：")
    print(arg1)
    print(var_args_dict)


printDic(21, name='tom', age=10)

# 声明函数时，参数中星号 * 可以单独出现
'''
如果单独出现星号 * 后的参数必须用关键字传入
'''


def sum(a, b, *, c):
    return a + b + c


# print(sum(10,20,30)) # sum() takes 2 positional arguments but 3 were given
print('sum = ', sum(10, 20, c=30))

# 3.匿名函数
'''
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数
语法
lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression
'''

sum1 = lambda a, b: a + b
print('相加后的值：', sum1(10, 20))
print('相加后的值：', sum1(20, 30))

# 4.return语句
'''
return [表达式] 语句用于退出函数，
选择性地向调用方返回一个表达式。
不带参数值的return语句返回None。
之前的例子都没有示范如何返回数值
'''


def sum2(arg1, arg2):
    total = arg1 + arg2
    print('函数内：', total)
    return total


total = sum2(10, 20)
print('函数外：', total)

# 5.变量作用域
'''
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是:
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）

以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），
再找不到就会去全局找，再者去内置中找
'''

'''
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
'''

# 5.1 全局变量和局部变量
'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
'''

amount = 0


def mount(arg1, arg2):
    amount = arg1 + arg2
    print('函数内局部变量：', amount)
    return amount


mount(10, 20)
print('函数外全局变量：', amount)

# 5.2 global 和 nonlocal关键字
'''
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''

price = 12.8
def discount():
    global price
    print(price)
    # 五折优惠
    price = 12.8 * 0.5
    print(price)

discount()
print(price)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()


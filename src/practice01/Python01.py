# 一、基础语法
# 1.1编码
"""
Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串
"""
# 1.2标识符
"""
①第一个字符必须是字母表中字母或下划线 _(不要带特殊字符如@#￥%&)
②标识符的其他部分是由字母、数字和下划线组成(不要带特殊字符如@#￥%&)
③标识符对大小写敏感
"""
# 1.3关键字
"""
# 如 False,None,True,as,assert,break,class,continue等
"""
# 1.4注释
'''
①Python中单行注释以 # 开头
#多行注释可以用多个 # 号，还有 \''' 和 """
'''
# 1.5行与缩进
'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
'''
if True:
    print("answer")
    print("true")
else:
    print("error")
    print("false")
# 1.6多行语句
'''
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠来实现多行语句
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠
'''
item_one="good good study"
item_two="day day up"
item_three="study"
total = item_one + \
        item_two + \
        item_three
print(total)
array = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(array)

# 数字类型
'''
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''





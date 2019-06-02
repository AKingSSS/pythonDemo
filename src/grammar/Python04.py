import random
import math

# 数字（number）
"""
Python 支持三种不同的数值类型
1、整型
2、浮点型
3、复数
"""
# 我们可以使用十六进制和八进制来代表整数
print(0xA0F)  # 十六进制
print(0o37)  # 八进制

# 1.数字类型转换
'''
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
'''
print("1.数字类型转换")
str1 = "13"
str2 = "03"
print(int(str1) + int(str2))
str3 = '19.01'
str4 = '0.09'
print(float(str3) + float(str4))
# 浮点数转整型
a = 1.3
print(int(a))  # --->> 1

# 2.数字运算
'''
在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // 
'''
print(2 / 3)  # --->>0.6666666666666666
print(1 / 2)  # --->>0.5

# 3.数字函数
'''
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)
如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根。
'''

# 4.随机函数
'''
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''
print("# 4.随机函数")
print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# abs(x) 与fabs(x)区别
'''
abs() 是一个内置函数，而 fabs() 在 math 模块中定义的。
fabs() 函数只适用于 float 和 integer 类型，而 abs() 也适用于复数。
'''
print(abs(-10.00))  # --->>> 10.0
print(abs(3 + 4j))  # --->>> 5.0 --->> 复数的绝对值即他的模 sqrt(3^2+(-4)^2)=5
print(math.fabs(-10.00))  # --->>> 10.0
# print(math.fabs(3 + 4j))  # --->> TypeError: can't convert complex to float

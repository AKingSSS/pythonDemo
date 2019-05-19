# if语句
"""
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
"""
'''
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

注意：

1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
'''

a = 1
while a < 10:
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
    a += 1
# -----------------------------------------
var1 = 100
if var1:
    print('1 - if 表达式条件为 true')
    print(var1)
var2 = 0
if var2:
    print('2 - if 表达式条件为 false')
    print(var2)
print('Good bye!')
# -----------------------------------------
age = int(input(" 请输入狗狗年龄："))
print('')
if age < 0:
    print('你是在逗我吧!')
elif age == 1:
    print('相当于 14 岁的人。')
elif age == 2:
    print('相当于 22 岁的人。')
else:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 数字猜谜游戏
number = 10
guess = -1
while number != guess:
    guess = int(input('请输入你猜的数字：'))
    if guess < number:
        print("你猜小了")
    elif guess > number:
        print('你猜大了')
    else:
        print('恭喜你 猜对了')

# ---------------------------------------------
num = int(input('请输入一个数字：'))
if num % 2 == 0:
    if num % 3 == 0:
        print('你输入的数字可以整除 2 和 3')
    else:
        print('你输入的数字可以整除 2，但不能整除 3')
else:
    if num % 3 == 0:
        print('你输入的数字可以整除 3，但不能整除 2')
    else:
        print('你输入的数字不能整除 2 和 3')

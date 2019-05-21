# 模块
"""
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
模块可以被别的程序引入，以使用该模块中的函数等功能
"""
# import sys
import Support
from .Price import price2

# print('命令行参数如下：')
# for i in sys.argv:
#     print(i)
# print('\\n\n python 路径为：', sys.path, '\n')

# 1.import 语句
'''
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]
'''
print(Support.amount(10, 5))
print(Support.amount2(100))

# from … import 语句
'''
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

from modname import name1[, name2[, ... nameN]]
'''
print(price2(300))



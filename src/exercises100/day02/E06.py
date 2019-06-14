"""
实例006：斐波那契数列
题目 斐波那契数列。

程序分析 斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。
图方便就递归实现，图性能就用循环。
1,1,2,3,5,8,13,21
"""


def Fib(n):
    if n <= 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


print(Fib(0))

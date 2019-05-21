def amount(price, discount):
    newPrice = ('{:.2f}'.format(price * discount / 10))
    return newPrice


def amount2(price):
    if price > 88:
        newPrice = ('{:.2f}'.format(price * 0.9))
    elif price > 188:
        newPrice = ('{:.2f}'.format(price * 0.8))
    elif price > 288:
        newPrice = ('{:.2f}'.format(price * 0.8))
    else:
        newPrice = price
    return newPrice

# __name__属性
"""
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
"""
# if __name__ == '__main__':
#     print('程序自身在运行')
# else:
#     print('我来自另一模块')

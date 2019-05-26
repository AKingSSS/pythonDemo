# File(文件) 方法
# 1.open() 方法
"""
Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

完整的语法格式为：

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

"""
f1 = open('D:\\ykDev\\pythonDemo\\file\\file1', 'rt')  # 需要用双斜杠\\
print(f1.readline())  # 读取整行，包括 "\n" 字符
print("-------------------------")
f1.close()

f2 = open('D:\\ykDev\\pythonDemo\\file\\file2', 'rt', encoding='utf-8')  # 需要用双斜杠\\
print(f2.read(1))  # 读取的是字符
f2.close()

# 文件分类
'''
文本文件：GBK、utf8、CP936

二进制文件：图像文件、音频文件、资源文件、office文档

open()函数返回1个可迭代的文件对象
如果指定文件不存在、访问权限不够、磁盘空间不足或者其他原因导致创建文件对象失败则抛出异常
当对文件内容操作完后，一定要关闭文件对象，这样才能保证所做的任何修改都确实保存到文件中
f2.close()如果在打开文件之后和关闭文件之前发生了错误导致程序崩溃，这是文件就无法正常关闭
在管理文件对象推荐使用with关键字，可以有效地避免这个问题
'''
with open('D:\\ykDev\\pythonDemo\\file\\file3','r') as src,open('D:\\ykDev\\pythonDemo\\file\\file2', 'w') as dst:
    dst.write(src)



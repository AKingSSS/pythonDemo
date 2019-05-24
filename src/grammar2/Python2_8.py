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

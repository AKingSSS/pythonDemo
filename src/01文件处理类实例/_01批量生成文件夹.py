import os

"""
在path目录下批量生成文件夹
"""
def MkDir():
    path = 'D:/ykDev/bajProject/JavaBasis/src/main/java/www/aking/com'  # 创建文件路径
    for i in range(4, 12):  # 创建文件个数
        file_name = path
        file_name_child = file_name + "/id{:02d}chapters".format(i)
        print("file_name_child = ", file_name_child)
        try:
            os.mkdir(file_name_child)
        except Exception as e:
            print('Exception', e)


MkDir()

import time

"""
实例009：暂停一秒输出
题目 暂停一秒输出。
"""
for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)

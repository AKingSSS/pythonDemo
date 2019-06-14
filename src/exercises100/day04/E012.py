import math

"""
实例012：100到200的素数
题目 判断101-200之间有多少个素数，并输出所有素数。

程序分析 判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。 用else可以进一步简化代码.
"""
count = 0
for i in range(100, 200):
    for j in range(2, round(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1

print("总共有", count, "素数")

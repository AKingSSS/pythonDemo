"""
实例004：这天第几天
题目 输入某年某月某日，判断这一天是这一年的第几天？

程序分析 特殊情况，闰年时需考虑二月多加一天：

"""


def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


DofM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
res = 0
year = int(input("Year: "))
month = int(input("Month："))
day = int(input("Day: "))
if isLeapYear(year):
    DofM[2] += 1
for i in range(month):
    res += DofM[i]
print("这一天是", year, "年的第", res + day, "天")

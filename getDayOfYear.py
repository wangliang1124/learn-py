import datetime


# 根据输入的年月日判断是当年中的第几天
def getDayOfYear():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    # print(type(date1),date2)
    index = (date1 - date2).days + 1
    print('{0}年的第{1}天'.format(year, index))
    return index


getDayOfYear()
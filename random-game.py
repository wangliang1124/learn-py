import random

print('猜数字游戏')
i = 1
a = random.randint(0, 10)
b = int(input('请输入0-10之间的数字'))

while a != b:
    if a > b:
        print('你输入的数字小于它')
        b = int(input('请再次输入'))
    else:
        print('你输入的数字大于它')
        b = int(input('请再次输入'))
    i += 1
else:
    print('恭喜猜中数字{0}，你猜了{1}次'.format(b, i))

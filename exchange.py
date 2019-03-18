# x = input('输入 x 值: ')
# y = input('输入 y 值: ')
 
# 方法一
# x,y = y,x


x = int(input('输入 x 值: '))
y = int(input('输入 y 值: '))

# 方法二 
# x = x + y
# y = x - y
# x = x - y

# 方法三
x = x ^ y
y = x ^ y
x = x ^ y
 
print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
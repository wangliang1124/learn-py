#!/usr/bin/env python3

'''
print('The quick brown fox', 'jumps over', 'the lazy dog')
print(100+200)
name = input('please enter your name: ')
print('hello,', name)
'''
'''
注释注释、////
'''

# print('The quick brown fox', 'jumps over', 'the lazy dog')
# print(100+200)
# name = input('please enter your name: ')
# print('hello,', name)

# 请问Python如何实现将列表：['a','a','b','a','b','c']输出为字典：{'a':3,'b':2,'c':1}?
# 方法一
# str_list = ['a', 'a', 'b', 'a', 'b', 'c']
# dic = {}
# for name in str_list:
#     result = dic.get(name, -1)
#     if result == -1:
#         dic[name] = 1
#     else:
#         dic[name] = dic[name] + 1
# print(dic)

# # 方法二
# str_list = ['a', 'a', 'b', 'a', 'b', 'c']
# dic = {}
# for i in str_list:
#     if str_list.count(i) >= 1:
#         dic[i] = str_list.count(i)
# print(dic)

# # 方法三
# str_list = ['a', 'a', 'b', 'a', 'b', 'c']
# s = set(str_list)
# # d = dict.fromkeys(s, 0)
# d = {}
# for i in s:
#     d[i] = str_list.count(i)
# print(d)


# a, b = 0, 1
# n = 40
# while n > 0:
#     print(b)
#     n -= 1
#     a, b = b, a+b


def f(n):
    a, b = 0, 1
    while n >= 2:
        n -= 1
        a, b = b, a+b
    print(b)

# f(40)
def getFib(n):
    if (n <= 2):
        return 1
    else:
        return getFib(n - 1) + getFib(n - 2)
# print(getFib(40))


def greetPerson(*name):
    print('Hello', name)
  
greetPerson('Runoob', 'Google')


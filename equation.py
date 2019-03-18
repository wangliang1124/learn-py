# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块
import cmath

print('求解一元二次方程 ax^2 + bx + c = 0')
a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))

d = b**2 - 4*a*c

s1 = (-b-cmath.sqrt(d)) / 2*a
s2 = (-b+cmath.sqrt(d)) / 2*a

print('解为{0} 和 {1}'.format(s1, s2))

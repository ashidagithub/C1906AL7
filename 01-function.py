# -*- coding: UTF-8 -*-

# Filename : 01-function.py
# author by : （学员ID)

# 目的:
# 掌握函数的用法

# 练习一：第一个函数
print('\n---华丽分割线---练习（1）---')
def hello():
    print("Function-Hello World!")
    return

# 调用
hello()

# 练习二：打印指定字符串 - 传入字符串
print('\n---华丽分割线---练习（2）---')
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return

# 调用
printme("xxxxx")

# 练习三：计算面积函数 - 传入数字
print('\n---华丽分割线---练习（3）---')
def area(width, height):
    return width * height

# 调用
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

# 练习四：将求三角形面积的海伦公式函数化
print('\n---华丽分割线---练习（4）---')
def triangle_area(a, b, c):
    # 依据海伦公式求任意三角形面积
    # 已知三角形三边a,b,c,半周长p,则S＝ √[p(p - a)(p - b)(p - c)] （海伦公式）（p=(a+b+c)/2）
    # 计算半周长
    p = (a + b + c) / 2

    # 计算面积
    # 掌握 python 开根号的写法
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area

# 调用
s = triangle_area(3,4,5)
print(s)

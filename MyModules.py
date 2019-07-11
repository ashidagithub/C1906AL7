# -*- coding: UTF-8 -*-

# Filename : 01-function.py
# author by : （学员ID)

# 目的:
# 掌握函数的用法

# 练习一：第一个函数


def hello():
    'Desc: Print hello world by function'
    print("Function-Hello World!")
    return

# 练习二：打印指定字符串 - 传入字符串


def printme(str):
    'Desc: Print a specified string'
    # 打印任何传入的字符串
    print(str)
    return

# 练习三：计算面积函数 - 传入数字


def area(width, height):
    'Desc: Calculate area'
    return width * height


'''
# 调用
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
'''

# 练习四：将求三角形面积的海伦公式函数化


def triangle_area(a, b, c):
    'Desc: Calculate triangle''s area '
    # 依据海伦公式求任意三角形面积
    # 已知三角形三边a,b,c,半周长p,则S＝ √[p(p - a)(p - b)(p - c)] （海伦公式）（p=(a+b+c)/2）
    # 计算半周长
    p = (a + b + c) / 2

    # 计算面积
    # 掌握 python 开根号的写法
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


'''
# 调用
s = triangle_area(3, 4, 5)
print(s)
'''

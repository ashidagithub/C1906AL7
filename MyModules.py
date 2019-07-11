# -*- coding: UTF-8 -*-

# Filename : 01-function.py
# author by : （学员ID)

# 目的:
# 掌握函数的用法


def hello():
    'Desc: Print hello world by function'
    print("Function-Hello World!")
    return


def cal_rect_area(width, height):
    'Desc: Calculate rectangle''s area'
    return width * height


def cal_triangle_area(a, b, c):
    'Desc: Calculate triangle''s area '
    # 依据海伦公式求任意三角形面积
    # 已知三角形三边a,b,c,半周长p,则S＝ √[p(p - a)(p - b)(p - c)] （海伦公式）（p=(a+b+c)/2）
    # 计算半周长
    p = (a + b + c) / 2

    # 计算面积
    # 掌握 python 开根号的写法
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


def pnt_cutline(sn):
    print('\n******我是新的华丽分割线(%d)******' % (sn))
    return


def pnt_str_with_cutline(sn, str):
    'Desc: Print a specified string, put a cutting line first'
    # 打印任何传入的字符串
    pnt_cutline(sn)
    print(str)
    return

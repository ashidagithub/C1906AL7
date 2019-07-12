# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 本模块为主模块，主程序，引用其他的模块
# ------------------------(max to 80 columns)-----------------------------------

from my_mods import *

# 输出一条分割线，然后打印一个 Hello World
pnt_cutline(1)
hello()

# 输出一条分割线，然后计算一个长方形的面积
pnt_cutline(2)
w = 5
h = 7
s = cal_rect_area(w, h)
print('长方形 宽为 %0.2f, 高为 %0.2f, 面积为 %0.2f' % (w, h, s))

result = '长方形 宽为 %0.2f, 高为 %0.2f, 面积为 %0.2f' % (w, h, s)
pnt_str_with_cutline(3, result)

# 按三角形的三条边计算三角形面积
side1 = 3
side2 = 4
side3 = 5
s = cal_triangle_area(side1, side2, side3)
result = '三角形 边长分别为 (%0.2f),(%0.2f),(%0.2f), 面积为 %0.2f' % (
    side1, side2, side3, s)
pnt_str_with_cutline(4, result)

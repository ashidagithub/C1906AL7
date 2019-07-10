# -*- coding: UTF-8 -*-

# Filename : 02-function-mutable.py
# author by : （学员ID)

# 目的:
# 掌握函数的用法

# 练习一： 对不可变参数的尝试
# 在 python 中，strings, tuples, 和 numbers 是不可更改的参数
# 函数说明：强制将传入的数字一律变为10
print('\n---华丽分割线---练习（1）---')
def ChangeInt( a ):
    a = 10
    return

# 妄图将 b 强制变成 10
b = 2
ChangeInt(b)
# print("\n------------华丽起始线------------")
print("强制改变了吗？ ",  b ) # 结果是仍然是 b 原值


# 练习二： 对可变参数的尝试
# 在 python 中，list, dict 是可以修改的参数
# 函数说明：对传入的列表进行改头换面处理
print('\n---华丽分割线---练习（2）---')
def changeme( inlist ):
    # 对传入的列表尾部强行添加一个数 50
    inlist.append(50)
    # 将传入的列表第一个值改为 99
    inlist[0] = 99
    return

# 调用changeme函数
mylist = [10,20,30,40]
changeme( mylist )
print("\n------------华丽分割线------------")
print ("强行添加且改变了吗？ ", mylist)

# 练习三： 利用 mutable  参数获得返回值
# 函数说明：获得一个指定范围内的奇数数列
print('\n---华丽分割线---练习（3）---')
def make_odd_list( limit, outlist ):
    for i in range(1, limit):
        if (i % 2) != 0:
            outlist.append(i)
    return

# 调用 make_odd_list 函数
mylist = []
make_odd_list(10, mylist)
print("\n------------华丽分割线------------")
print ("输出数列为", mylist)

# 练习四： 利用 mutable  参数获得返回值
# 函数说明：获得2个指定范围内的数列（奇数数列+偶数数列）
print('\n---华丽分割线---练习（4）---')
def make_2_list( limit, outlist1, outlist2 ):
    for i in range(1, limit):
        if (i % 2) != 0:
            outlist1.append(i)
        else:
            outlist2.append(i)
    return

# 调用 make_2_list 函数
mylist1 = []
mylist2 = []
make_2_list(20, mylist1, mylist2)
print("\n------------华丽分割线------------")
print ("输出奇数列为", mylist1)
print ("输出偶数列为", mylist2)

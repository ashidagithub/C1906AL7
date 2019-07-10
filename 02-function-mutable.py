# -*- coding: UTF-8 -*-

# Filename : 02-function-mutable.py
# author by : （学员ID)

# 目的:
# 掌握函数的用法

# --------------------------------------------------------
# 练习一： 对不可变参数的尝试
# 在 python 中，strings, tuples, 和 numbers 是不可更改的参数
# 函数说明：强制将传入的数字一律变为10
def ChangeInt(a):
    a = 10
    return


# 妄图将 b 强制变成 10
b = 2
ChangeInt(b)
# print("\n------------华丽起始线------------")
print('\n-----------cutting line(1)---------------')
print("强制改变了吗？ ",  b)  # 结果是仍然是 b 原值


# --------------------------------------------------------
# 练习二： 对可变参数的尝试
# 在 python 中，list, dict 是可以修改的参数
# 函数说明：对传入的列表进行改头换面处理
def change_me(inlist):
    # 对传入的列表尾部强行添加一个数 50
    inlist.append(50)
    # 将传入的列表第一个值改为 99
    inlist[0] = 99
    return


# 调用changeme函数
myList = [10, 20, 30, 40]
change_me(myList)
print('\n-----------cutting line(2)---------------')
print("强行添加且改变了吗？ ", myList)

# --------------------------------------------------------
# 练习三： 利用 mutable  参数获得返回值
# 函数说明：获得一个指定范围内的奇数数列
def make_odd_list(limit, outlist):
    for i in range(1, limit):
        if (i % 2) != 0:
            outlist.append(i)
    return

# 调用 make_odd_list 函数
myList = []
make_odd_list(10, myList)
print('\n-----------cutting line(3)---------------')
print("输出数列为", myList)

# --------------------------------------------------------
# 练习四： 利用 mutable  参数获得返回值
# 函数说明：获得2个指定范围内的数列（奇数数列+偶数数列）
def make_2_list(limit, outlist1, outlist2):
    for i in range(1, limit):
        if (i % 2) != 0:
            outlist1.append(i)
        else:
            outlist2.append(i)
    return

# 调用 make_2_list 函数
myList1 = []
myList2 = []
myLimit = 100
make_2_list(myLimit, myList1, myList2)
print('\n-----------cutting line(4)---------------')
print('输出 %d 以内的奇数和偶数数列' % (myLimit))
print("输出奇数列为", myList1)
print("输出偶数列为", myList2)

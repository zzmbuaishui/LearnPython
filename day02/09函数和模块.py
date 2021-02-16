#  写一个方法

# def sum_zzm(x, y):
#     print(x)
#     print(y)
#     su = x + y
#     print(type(su))
#     print("结果是%d" % su)
#     return su
#
#
# x = int(input("输入一个x"))
# y = int(input("输入一个y"))
# sum_zzm(x, y)
# 函数传参
#
# from random import randint
#
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     """三个数相加"""
#     return a + b + c
#
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))


# 可变参数

def add(* args):
    # 获取参数
    for x in args:
        print(x)

add(1,12,23,43,4)
# suma = 0
# 0到100 相加
# for x in range(101):
#     suma += x
#     print(suma)
# for x in range(0, 101, 2):
#     suma += x
#     print(suma)
# 猜数字，利用随机函数
import random

is_sum = 0
is_im = int(input("输入数字"))
is_for = True
while is_for:
    print("看看随机多少次才能出来！！")
    rd = random.randint(0, 100)
    if rd == is_im:
        print("已经出结果了")
        print('你总共猜了%d次' % is_sum)
        break
    else:
        print("没有成功... ...")
        is_sum += 1

# user_name = input("输入姓名")
# user_pass = input("输入密码")
#
# if user_pass == "zzm" and user_name == "zzm":
#     print("登录成功")
#     print("... ...")
# else:
#     print("登录失败")
#     print("... ...")




# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
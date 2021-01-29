# 1.学习一个python 从第一个hello world !  开始
#print("hello world !")
# 2.查看一下python 版本
# import sys
# print(sys.version_info)
# print(sys.version)
# 3.注释 单行注释 ctrl + /
# 4.多行注释
# ''' 多行注释'''
# """ 多行注释 """
# 5.作者给出的语录
# import this 
# 6.简单的小代码  使用turtle在屏幕上绘制图形
# import turtle
# # 画布就是turtle为我们展开用于绘图区域，我们可以设置它的大小和初始位置。
# turtle.screensize(800,600,"green")
# # 设置画笔的宽度
# turtle.pensize(55)  
# # 当前画笔颜色   
# turtle.pencolor('red')   
# 画一个花
import turtle
# 画多少笔
for i in range(100): 
    turtle.pencolor('red') 
    # 向前移动i 长度
    turtle.forward(i)
    # 向左移动91
    turtle.right(91)
         
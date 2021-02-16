b = 12.345
# 将一个数值或字符串转换成整数
bz = int(b)
print(type(bz))
# 将一个字符串转换成浮点数
bz = float(b)
print(type(bz))
# 将指定的对象转换成字符串形式
bz = str(b)
print(type(bz))
# 将字符串（一个字符）转换成对应的编码（整数）
b = "n"
# 转换失败报错 必须是string
bz = ord(b)
print(type(bz))
# 将整数转换成该编码对应的字符串（一个字符）
b = 13
bz = chr(b)
print(type(bz))

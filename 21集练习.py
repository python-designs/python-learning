from time import sleep
"""
1 + 1
'1' + '1'
[1, 2] + [3, 4]


4 - 3

print("2" - "1")
print([3, 4] - [2, 3])
这两个不行的原因，你的目的想法是否符合python使用手册

print(3 * 3)
print(3 ** 3)

print(5 / 2)
print(5 / 0)
print(5 // 2) # 整除

print(5 % 2) # 求余运算

a = 10
b = a + c
a, b, c = 10, 29, 23

# 运算符优先级,小括号到乘除到加减
result = 1 + 2 * 3 / 4

num = 4
low = num // 4


num = 10
bum = 10
# is是比较唯一标识
print(id(num),id(bum))
print(bum is num)

a = [1]
b = [2]
print(a == b)
print(a is b)
print(5 < num < 20)



# 逻辑数据
b = True
print(not b)
print(not 1)
print(1 and 3)
print(0 or 3)
print(True and True)
print(True and False)
print(True or False)
print(bool(11))
print(bool("0"))

print(bool())
print(bool(""))

content = input("请输入内容： ")
print(type(content))
#try:
#    content = int(content)
# except ValueError:
#    print("请输入数字")

content = eval(content)
print(type(content))
print(content)

your_name = input("你的名字")
your_age = eval(input("你的年龄"))
print("这是你的名字%s，这是你的年龄%d" % (your_name, your_age))
# 改成格式化输出则为
print("这是你的名字{0}，这是你的年龄{1}".format(your_name, your_age))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度') # 这个方便


# 输出到文件中
# print >>open("test.txt", "w", "12345")
f = open("test.txt", "w") # 这个是创建了一个文件如果之前有要删除
print("1234", file=f)

# 默认情况先导入文件 import sys 然后print("1234", file=sys.stdout)这边的标准输出是控制台

print('请输入账号', end='')
print('请输入账号\n', end='')# 但是没用
# 如果最后是换行那么缓冲区里面的东西直接到控制台
sleep(5)
"""
# 解决方法
print('请输入账号', end='', flush=True)

# 站位符的补充，类型码有哪些
# %[(name)][flags][width][.precision]typecode
# []:可以省略
# (name)，根据制定的名称(key),查找对应的值，格式化到字符串中
MathScore = 59
EngLishscore = 58
print("我是数学分数是%d,英语分数是%d" % (MathScore, EngLishscore))
print("我是数学分数是%(ms)d,英语分数是%(es)d" % ({"ms": MathScore, "es": EngLishscore}))

# width,表示占用宽度
print("%10d" % MathScore)

# flags
print("%-10d" % MathScore)
# 空一格和空两个格子区别
print("% d" % MathScore)
print("%  d" % MathScore)


min2 = 50
sec = 8
print("%02d:%02d" % (min2, sec))

# .precision小数点后精度
f_Score = 59.9
print("%.2f", f_Score)

print("%c" % 2323)
print('%d%%' % 99)


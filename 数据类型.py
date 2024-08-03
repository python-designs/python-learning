import math
import random
# 复数的表达形式
x = complex(1.1, 2.22)
print(x)

# 进制转换
num = 0o17
print(num)

num = 18
print(hex(num))

# 非零即真，非空即真


n1 = 11
n2 = 2.3
result = n1 + n2
print(type(result))
# 因为浮点类型的精度高于int类型的精度


# 开始使用python内建函数(这次是对于数值类型的操作)，直接使用的关键字应该就是内置函数里面的

# 绝对值
num = -10
print(abs(num))

#最大值
print(max(1, 20, 320, 2321))

#最小值
print(min(1, 20, 320, 2321))
print(min([1, 232, 3232, 232]))

# 四舍五入
p = 3.147
print(round(p, 2))

# pow(x,y), 返回x的y次幂
print(pow(2, 4, 7))  # 这个还可以取模运算2 ** 4 % 7
print(2 ** 4)


# 开始使用数学库

# 上取整
p1 = 3.4
print(round(p1))
print(math.ceil(p1))

# 下取整
p2 = 3.9
print(math.floor(p2))


# 根号/开平方
print(math.sqrt(9))

# 求对数
print(math.log(10000, 10))  # 10的多少次方等于10000


# 随机函数库

# 取小数，在0~1的区间里面，[0, 1)
print(random.random())


# 从序列中随机挑选一个数值
print(random.choice([1, 32, 23, 4, 34]))

# 还有一些不常用的看58的7.16

# 最后再讲一个常用的
p1 = random.randrange(1, 101, 2)
print(p1)


# 三角函数的使用

# sin(30)，里面的30是弧度
# 数学常量，一般在c里里面是加const,但在python里面是只能约定，通过口头上面
jiao = int(input("输入度"))
jiao = jiao / 180 * math.pi
result = math.sin(jiao)
print(result)

# 或者用函数将角度转成弧度或者弧度转成角度
jiao = math.radians(int(input("输入角度")))
result = math.sin(jiao)
print(result)



# 开始bool类型
# 是int类型的子类，有一部分int特性

# 可以参加运算
print(True + 2)
print(False + 2)  # 还是遵从非零即真，非空即真

# 比较表达式的运算结果，；例如：3 > 2

# 用于if或while循环条件
while True:
    print("无限循环")

if True:
    print("真")

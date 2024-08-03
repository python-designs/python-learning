from time import sleep

"""
num = 0
while num < 10:
    print("设计")
    num += 1
    sleep(0.1)

i = eval(input("从几开始"))
# num = 0
# num = float(num)
改成 num = 0.0
j = float(input("你需要几个数字的和")) # eval改成float
while i < j:   # 或者i ！= 10

print("%f", num)



i = 0
while i < 3:
    i += 1
    print("正常")
    break
else:
    print("最后的i = ", i)
    print("整个循环已经执行完毕")



# for 一般遍历的是一个集合
pats = "1, 2, 3, 4, 5"
i = 0
for c in pats:
    i += 1
    print("循环次数", i)
    # 如果加入break就回直接跳出
else:
    print(c)



# 反转字符串

# 我思考的但有问题
str1 = "社会我孙工，人狠话不多"
i = 0
for num in str1:
    i += 1
    if num == " ":
        i -= 1
    print(i)
while i > 0:
    print(str1[i])
    i -= 1

# ai写的
# 反转字符串
str1 = "社会我孙工，人狠话 不多"
# 初始化索引为字符串长度
i = len(str1) - 1

# 打印反转后的字符串
for num in str1:
    if num != ' ' and i >= 0:
        print(str1[i])  # 使用 end='' 防止打印换行符
    else:
        num = ""
        print(str1[i])
    i -= 1  # 递减索引以反转字符串




# 反转字符串并去掉空格
str1 = "社会我孙工，人狠话  不多"

# 初始化索引为字符串长度
i = len(str1) - 1
reversed_str1 = ''

# 打印反转后的字符串
while i >= 0:
    if str1[i] != ' ':
        reversed_str1 += str1[i]
    i -= 1

print(reversed_str1)


# 视频给的
notice = "社会我孙工，人狠话不多"

result = ""
for c in notice:
    result = c + result# c + result 和 result + c 是不一样的

print(result)



# 打印偶数
num = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        num += i
    i += 1
print(num)


for i in range(1, 11): # 11之前的数字到11就停
    if i == 6:
        # break
        continue
    print(i)



while True:
    num1 = eval(input("输入数字"))
    num1 = float(num1)
    num2 = eval(input("输入数字"))
    num2 = float(num1)
    if num1 > 100 or num2 > 100:
        # print("数据输入有问题")
        # continue
        break
    result = num1 + num2
    print(result)
    answer = input("是否想要退出")
    if answer == "是":
        break
    else:
        continue



nums = range(1, 10)
for num in nums:
    if num % 2 == 0:
        print(num)
    else:
        print("该数字是奇数")


# 外层循环执行一次，内部循环执行全部
for i in range(1, 6):
    for j in range(1, 3):
        print(j)

# 九*九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(i, j)
        print(i * j)



level = eval(input("第几层"))
level = max(1, level)# 如果小于1将他设置为1
num = eval(input("从几开始"))
num = max(1, num)
# 是外循环的数乘内循环，就乘一次但是跟外循环第一次乘的数无关
# for i in range(1, 10):
#     for j in range(1, 10):
# 比如说这个外循环的{1 * 内循环的range(1, 10)}然后再依次排列
for i in range(num, level + 1):
    for j in range(1, i + 1):
        # print(i, j)
        # print(i * j)
        # 换成
        print("%d * %d = %d" % (i, j, i * j), end="\t")# \t 就是tab
    print("\n")
"""









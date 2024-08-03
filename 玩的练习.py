import math
"""
print(0b100)
print(0o100)
print(100)
print(0x100)

print(1.2345e2)  # 科学计数法

a = 0
print(type(a))


f = float(input("请输入华氏温度： "))
c = (f - 32) * 5.0 / 9.0
# print("华氏温度为%f,对应的摄氏温度为%f" % (f, c))
print(f"{f:.1f}华氏度 = {c:.1f}摄氏度")


radius = float(input("输入圆的半径"))
perimeter = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print(f"圆的周长{perimeter:.1f}， 圆的面积{area:.1f}")
# 还有一种格式化输出
print(f"{area = :.1f}")
# 不好用，不能用文字，相当于只是把area这个变量算出来了
"""

"""
high = float(input("身高多少厘米： "))
weight = float(input("体重多少千克： "))
BMI = weight / (high / 100) ** 2
print(f"你的BMI为{BMI:.3f}")

match BMI:
    case 18.5 <= BMI < 25:
        print("你的身材很棒")
    case 25 <= BMI < 27:
        print("你的体重过重！")
    case 27 <= BMI < 30:
        print("你已轻度肥胖！")
    case 30 <= BMI < 35:
        print("你已中度肥胖！")
    case _:
        print("你的体重过轻或数据输入有误")

if 18.5 < BMI < 25:  # 关系运算会产生布尔值
    print("你的身材很棒")
elif BMI < 24:
    print('你的身材很棒！')
elif BMI < 27:
    print('你的体重过重！')
elif BMI < 30:
    print('你已轻度肥胖！')
elif BMI < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')




status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405:
        description = 'Invalid Request'
    case 401 | 403 | 404:  # 不同数值归入一个分支
        description = 'Not Allowed'
    case _:
        description = 'Unknown Status Code'
print('状态码描述:', description)

# Flat is better than nested，扁平化，可读性更重要
x = float(input("x = "))
if x > 1:
    y = x * 3 - 2
elif x < 1:
    y = x * 8
else:
    y = x + 12
print(f"y = {y:.2f}")



i = 0
for num in range(1, 101):
    i += num
print("1~100整数和为%d" % i)



i = 0
for num in range(0, 101, 2):
    i += num
print("1~100偶数和为%d" % i)

# 或者是
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(f"1~100的偶数和为%d" % total)

print(sum(range(0, 101, 2)))
"""








high = eval(input("你的身高(m)："))
high = float(high)
weigh = eval(input("你的体重(kg)："))
weigh = float(weigh)
age = eval(input("你的年龄："))
age = int(age)
sex = input("你的性别")
sex = str(sex)
if sex == "男":
    sex2 = 1
elif sex == "女":
    sex2 = 0

BMI = weigh / (high * high)


def rich(BMI, age, sex2):
    rich_number = 1.2 * BMI + (0.23 * age) - 5.4 - (10.8 * sex2)
    return rich_number


result = rich(BMI, age, sex2)
print("%.2f" % result)
"""
if (sex == "男" and 15 < result < 18) or (sex == "女" and 15 < result < 18):
    print("正常")
else:
    print("不正常")
"""

if sex == "男":
    if 15 < result < 18:
        print("正常")
    else:
        print("不正常")

if sex == "女":
    if 25 < result < 28:
        print("正常")
    else:
        print("不正常")


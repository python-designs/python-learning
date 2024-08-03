import random

# {}中需要至少有一个元素，因为没有元素的{}并不是空集合而是一个空字典
# 但是我们可以用set来创建空集合，set()
# set 就是来构造一个具有无序性，确定性，互异性的篮子的模子
set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {'banana', 'pitaya', 'apple', 'banana', 'grape'}
print(set2)
# 输出无序性，呵呵
# 至于为什么输出是 {'apple', 'grape', 'pitaya', 'banana'} 这样的顺序，这是因为集合是无序的。Python 的集合不保证元素的顺序，每次迭代或打印集合时元素的顺序都可能不同。集合的这种特性使得它非常适合用于存储不希望重复的元素集合，但不适合用于需要保持元素顺序的场景。

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

"""
集合中的元素必须是hashable类型，使用哈希存储的容器都会对元素提出这一要求。
所谓hashable类型指的是能够计算出哈希码的数据类型，通常不可变类型都是hashable类型，
如整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）等


因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。例如：我们不能将列表作为集合中的元素；
同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。
我们可以创建出嵌套的列表，但是我们不能创建出嵌套的集合，
这一点在使用集合的时候一定要引起注意。
"""

set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
print(len(set1))
for elem in set1:
    print(elem)

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)

# 有一种不可变集合叫frozenset，可以用于哈希


# 开始字典教程
person1 = {
    "name": '王大锤',
    'sex': True,
    'birth': '1999-12-12',
    'height': 168,
    'weight': 65,
    'addr': '成都市武侯',
    'sb': 'txx',
    'doing': 'ipone bomb',
    "ipone": ['12324324324', '324324324234'],
    'car': {
        'brand': 'bmi',
        'max_speed': '239',
        'drive_type': "4wd",
    }
}

print(person1)


# 在元组里面讲的构造式也可以用在集合里面
person2 = dict(name='孙小美', birth='1999-12-12', age='32', tles='23232442342')
print(person2)

items1 = dict(zip('ABCDE', range(1, 6)))
print(items1)
# zip() 函数用于将多个可迭代对象（如列表、元组、字符串等）中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的迭代器。在创建字典时，zip() 经常与 dict() 一起使用，以快速生成字典的键值对。
items2 = dict(zip('ABCDE', range(1, 11)))

# 集合的生成式语法
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)
items33 = {x: (x + 3) ** 2 for x in range(1, 6) if x % 2 != 0}
print(items33)

# 通过两个循环你就知道为什么要叫键值对了
for key in person1:
    print(key, person1[key])
print("-" * 20)
for value in person2.values():
    print(value)
# 过程中有个思路，如何让他们相互匹配

# 思路突破的关键知识点：.items() 方法是字典（dict）的一个内建方法
# key, value是二元组
for key, value in person2.items():
    print(key, value)
# 这是两种操作
for key in person2:
    print(key, person2[key])
print("-" * 20)























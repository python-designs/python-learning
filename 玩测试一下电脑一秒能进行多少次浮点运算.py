
import time
import math
'''
def test_flops(iterations):
    start_time = time.time()

    # 执行浮点运算：计算数学常数 e 的近似值
    sum_result = 1.0
    for i in range(iterations):
        sum_result += math.exp(-i/float(iterations))

    end_time = time.time()

    elapsed_time = end_time - start_time
    flops = iterations / elapsed_time

    return flops

# 设置要测试的迭代次数
iterations = 1000000  # 您可以根据需要调整这个值

# 执行测试并打印结果
flops_per_second = test_flops(iterations)
print(f"在 {iterations} 次迭代中，每秒大约可以进行 {flops_per_second:.2f} 次浮点运算（FLOPS）。")
'''
# 三引号（'''），这通常用于定义多行（跨行）字符串。
# 三引号可以是单引号 ''' 或双引号 """，它们允许字符串跨越多行，
# 同时保留字符串中的所有空白字符，包括换行符。

# s3 = '''hello,
# wonderful
# world!'''
# print(s3)
# print(type(s3))

'''
# 转义字符
print()
print("\n")
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)


# 原始字符串
print("\n")
print(r"\n")

s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)
'''
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))            # rod函数是查询对应的编码，39558
print(ord('昊'))            # 26122









#  切片修改只能在列表上，最起码字符串和元组不能

# 字符串
s1 = 'hello' + ',' + 'world'
print(s1)

# 字符串的给对象发消息
s1 = 'hello,world'
print(s1.capitalize())
print(s1.title())
print(s1.upper())
s2 = 'GOODBYE'
print(s2.lower())
print(s1)
print(s2)
# 由于字符串是不可变类型，使用字符串的方法对字符串进行操作会产生新的字符串，但是原来变量的值并没有发生变化。
# 所以上面的代码中，当我们最后检查s1和s2两个变量的值时，s1和s2 的值并没有发生变化。




# find和index用法跟在列表里面的一样


# 格式化输出
a = 123
b = 232
print(f'{a} * {b} = {a * b}')

# 修剪操作，这让我想起了之前反向打印一个字符串时候的情况
# 当时我设想的是如果有空格怎么办，结果弄的很麻烦
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界

# 字符串是不可变容器的数据类型，不能用切片索引来替换内容，那为什么可以用replace函数来替换
"""
为什么可以使用 replace 方法：
replace 是字符串类型的一部分，专门为了在字符串中查找和替换子字符串而设计的。
它提供了一种方便的方式来执行替换操作，而不需要手动使用切片和连接。
使用 replace 方法可以减少代码量，提高代码的可读性和易用性。
不可变类型的特性：
不可变类型（如字符串和元组）的值一旦创建就不能被改变。
任何看似修改了不可变类型操作实际上都是创建了一个新的对象。
因此，尽管字符串是不可变的，Python 提供了如 replace 这样的方法来允许我们以一种安全和高效的方式来处理字符串内容的变更，同时保持原始数据的不变性。
"""
'''
s = 'hello,good world'
print(s.replace('o', '@'))
print(s.replace('o', '@', 1))



# 拆分和合并
# 可以用替换函数修改字符串，也可以用拆分和合并来修改字符串


s = 'I love you'
words = s.split()
print('~'.join(words))

s = 'I#love#you#so#much'
words = s.split('#')
print(words)
words = s.split('#', 2)
print(words)


#编码和解码
# Python 中除了字符串str类型外，还有一种表示二进制数据的字节串类型（bytes）。所谓字节串，就是由零个或多个字节组成的有限序列。通过字符串的encode方法，我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的decode方法，将字节串解码为字符串，代码如下所示。

a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊
'''

s = ['hello world', 'hallo worf']
s1 = s.strip()
print(s1.find('o'))
print(s1.startswith('he'))
print(s1.endswith('ld'))
print(s1.isalpha())
print(s1.rjust(20))




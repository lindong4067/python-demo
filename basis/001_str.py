s1 = 'asdfgh'
s2 = 'qwerty'
# 首字母大写
s1 = s1.capitalize()
print(s1)
# 所有变小写，casefold更牛逼，很多未知的对相应变小写
s2 = s1.casefold()
print(s2)
s3 = s1.lower()
print(s3)
# 设置宽度，并内容居中
# 20 代指总长度
# *  空白未知填充，一个字符，可有可无
test = 'aLex'
v = test.center(20, '*')
print(v)

# 去字符串中寻找，寻找子序列的出现次数
test = "aLexalexr"
v = test.count('ex')
print(v)
v = test.count('ex', 5, 6)
print(v)

# 以什么什么结尾
# 以什么什么开始
test = "alex"
v = test.endswith('ex')
print(v)
v = test.startswith('ex')
print(v)

# 从开始往后找，找到第一个之后，获取其未知
# > 或 >=
test = "alexalex"
# 未找到 -1
v = test.find('ex')
print(v)

# 格式化，将一个字符串中的占位符替换为指定的值
test = 'i am {name}, age {a}'
print(test)
v = test.format(name='alex', a=19)
print(v)

test = 'i am {0}, age {1}'
print(test)
v = test.format('alext', 19)
print(v)

# 字符串中是否只包含 字母和数字
test = "123"
v = test.isalnum()
print(v)

# 是否是字母，汉字
test = "as2df"
v = test.isalpha()
print(v)

# 13 当前输入是否是数字
test = "二" # 1，②
v1 = test.isdecimal()
v2 = test.isdigit()
v3 = test.isnumeric()
print(v1,v2,v3)

# 是否存在不可显示的字符
# \t    制表符
# \n    换行符
test = "oiuas\tdfkj"
v = test.isprintable()
print(v)
test = ' '
v = test.isspace()
print(v)

# 16 判断是否是标题
test = "Return True if all cased characters in S are uppercase and there is"
v1 = test.istitle()
print(v1)
v2 = test.title()
print(v2)
v3 = v2.istitle()
print(v3)

# 17 ***** 将字符串中的每一个元素按照指定分隔符进行拼接
test = "你是风儿我是沙"
print(test)
v = "_".join(test)
print(v)

# 18 判断是否全部是大小写 和 转换为大小写
test = "Alex"
v1 = test.islower()
v2 = test.lower()
print(v1, v2)

v1 = test.isupper()
v2 = test.upper()
print(v1, v2)

# 19
# 移除指定字符串
# 有限最多匹配
test = "xa"
v = test.lstrip('xa')
v = test.rstrip('9lexxexa')
v = test.strip('xa')
print(v)

test.lstrip()
test.rstrip()
test.strip()
# 去除左右空白
v = test.lstrip()
v = test.rstrip()
v = test.strip()
print(v)
print(test)
# 去除\t \n
v = test.lstrip()
v = test.rstrip()
v = test.strip()
print(v)

# 21 分割为三部分
test = "testasdsddfg"
v = test.partition('s')
print(v)
v = test.rpartition('s')
print(v)

# 22 分割为指定个数
v = test.split('s', 2)
print(v)
v = test.rsplit()
print(v)

# 25 大小写转换
test = "aLex"
v = test.swapcase()
print(v)

# 26 字母，数字，下划线 ： 标识符 def  class
a = "defeee"
v = a.isidentifier()
print(v)

# 27 将指定字符串替换为指定字符串
test = "alexalexalex"
v = test.replace("ex", 'bbb')
print(v)
v = test.replace("ex", 'bbb', 2)
# 2: 替换前几个
print(v)

# join       # '_'.join("asdfasdf")
# split
# find
# strip
# upper
# lower
# replace

# 一、for循环
# for 变量名 in 字符串:
#     变量名
# break
# continue


# index = 0
# while index < len(test):
#     v = test[index]
#     print(v)
#
#     index += 1
# print('=======')

# for zjw in test:
#     print(zjw)

# test = "郑建文妹子有种冲我来"
# for item in test:
#     print(item)
#     break

# for item in test:
#     continue
#     print(item)

# 二、索引，下标，获取字符串中的某一个字符
# v = test[3]
# print(v)

# 三、切片
test= 'abcdef'
v = test[0:-1]
# 去掉最后一个
# 0=<  <1
print(v)
v = test[0:1]
print(v)

# 五、获取连续或不连续的数字，
# Python2中直接创建在内容中
# python3中只有for循环时，才一个一个创建
r1 = range(10)
for r in r1:
    print(r)
r2 = range(1, 10)
for r in r2:
    print(r)
r3 = range(1, 10, 2)
for r in r3:
    print(r)

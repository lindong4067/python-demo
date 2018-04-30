#!/usr/bin/python3
import re

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
	print ("matchObj.group() : ", matchObj.group())
	print ("matchObj.group(1) : ", matchObj.group(1))
	print ("matchObj.group(2) : ", matchObj.group(2))
else:
	print ('No match!')

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
	print ("searchObj.group() : ", searchObj.group())
	print ("searchObj.group(1) : ", searchObj.group(1))
	print ("searchObj.group(2) : ", searchObj.group(2))
else:
	print ('No search!')

## 正则表达式修饰符
#	re.I
#	re.L
#	re.M
#	re.S
#	re.U
#	re.X

## 正则表达模式
#	（+ ? . * ^ $ ( ) [ ] { } | \ ）当控制符时需要转义

# 	表达式示例				匹配
#	python					python
#	[Pp]ython				Python python
#	rub[ye]					ruby rube
#	[aeiou]					a e i o u
#	[0-9]					0 1 2 3 4 5 6 7 8 9
#	[a-z]
#	[A-Z]
#	[a-zA-Z0-9]
#	[^aeiou]				匹配除元音字母之外的任何东西
#	[^0-9]					除数字之外的任何东西
#	.						除换行符之外的任何字符
#	\d						[0-9]
#	\D						[^0-9]
#	\s						[\t\r\n\f]
#	\S						[^\t\r\n\f]
#	\w						[A-Za-z0-9_]
#	\W						[^A-Za-z0-9_]
#	ruby?					rub ruby
#	ruby*					rub ruby rubyy...
# 	ruby+					ruby rubyy rubyy...
#	\d{3}					三位数字 123 456 789
# 	\d{3,}					三位或更多位数字
#	\d{3,5}					三位，四位，五位数
#	<.*>					贪婪匹配 <pythpn><perl>
# 	<.*?>					非贪婪匹配<python>
#	\D\d+					+ 作用于 \d
#	(\D\d)+					+ 作用于 \D\d
#	([Pp]ython(,)?)+		匹配“Python”，“Python, python, python”

#	([Pp]ython&\1ails)		Python&Pails python&pails
#	(['"])[^\1]*\1			单引号或双引号字符串

#	python|perl				python perl
#	rub(y|le)				ruby ruble
#	Python(!+|\?)			Python! Python!! Python!!... Python?

#	^Python					在字符串或内部行的开头匹配“Python”
#	Python$					在字符串或内部行的结尾匹配“Python”
#	\APython				在字符串的开头匹配“Python”
#	Python\Z				在字符串的末尾匹配“Python”
#	\bPython\b				在字词的边界匹配“Python”
#	\brub\B					\B是非字词边界：在“rube”和“ruby”中匹配“rub”，而不是单独匹配
# 	Python(?=!)				匹配“Python”，如果跟着感叹号。
#	Python(?!!)				匹配“Python”，如果没有感叹号后面。
#	R(?#comment) 			匹配“R”。其余的都是注释
# 	R(?i)uby 				匹配“uby”时不区分大小写
# 	R(?i:uby) 				同上


#!/usr/bin/python3

import os
os.getcwd()	#返回当前的工作目录
os.chdir('~')	#修改当前的工作目录
os.system('mkdir LD')	#执行系统命令

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('~/LD' 'LD')

import glob
glob.glob('*.py')
#['primes.py', 'random.py', 'quote.py']

import sys
print sys.argv
#['demo.py', 'one', 'two', 'three']

import re
re.findall(r'\b[a-z]', 'which foot or hand fell fastest')
#['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
#'cat in the hat'
'tea for too'.replace('too', 'two')

import random
random.choice(['apple', 'pear', 'banana'])
# 'apple'
random.sample(range(100), 10)   # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
random.random()    # random float
#0.17970987693706186
random.randrange(6)    # random integer chosen from range(6)
# 4

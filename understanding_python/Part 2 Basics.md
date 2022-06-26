# Part 2 Basics

## 2.1 Hello World

#### program hello_world.py

```commandline
python –c "import hello_world"  # run as import, no print     #  __name__ == "hello_world"
python –m hello_world  # run module as a script   #  __name__ == "__main__"
Hello World
python hello_world.py   # run script(as main module) #  __name__ == "__main__"
Hello World
python –i hello_world.py  # -i option can enter interactive mode after program is done #  __name__ == "__main__"
Hello World
>>> __name__
'__main__'
```

## 2.2 Statement and Comments

#### Statement

```python
a,b,c,d = 0,0,0,0
if a == 1 or b == 1 or c == 1 \
or d == 1:
    pass

if (a == 1 or b == 1 or c == 1 
or d == 1):
    pass
```
#### Comments

```python
#! /usr/bin/python # add #! with a path to specify interpreter
# -*- coding:utf-8 -*- # add coding type at first line or second line

# single line comment
"""
multiple lines comments
multiple lines comments
"""
```

## 2.3 Expressions and Assignment

#### Expressions

```python
3   # value = 3
3 * 2 + 1  # value = 7
3, 4   # value = (3, 4)
["abc", 1]  # value = ["abc", 1]
8 > 0  # value = True
abs(-2) + 3  # value = 5
1 << 3  # value = 8
3 + 1 == 5  # value = False
a > b and c > d # bool expression
a > b > c > d == 20  # bool expression
```

#### Assignment

```python
# single target
a = 5
# multiple target
b, c = 8, 9
d, (e, f) = a, (b, c)
first, *_, last2, last = [1, 2, 3, 4, 5, 6]
# target is attribute reference
a.x = 5
# target is subscription
a[0] = 8
b["cat"] = b["cat"] + 1
# target is slicing
a[1:3] = [6, 7]
```

## 2.4 Condition and Loop Statement

#### Condition

```python
# Condition statement
a = 1
if a > 0:
    print(a)
else:
    print(-a)
    
# if else expression
print(a if a > 0 else -a)

# enclosed if statement
b = 1
if a < 1:
    print("a < 1")
elif a < 2:
    print("a < 2")
    if b > 0:
        print ("b > 0")
else:
    print("a >= 2")

# While statement with break
a = 1
while True:
    a += 1
    if a % 2 == 0:
        print("event number: %d" %a)
    if a > 100:
        break

# While statement with continue
a = 1
while a <= 100:  
    a += 1
    if a % 2 == 1:
        continue
    print("even number: %d" % a)

# 
```
* If else expression:
    * c++: a >= 0 ? a : -a
    * python: a if a >= 0 else -a

#### Loop

```python
my_list = [1, 2, 3]
# for loop with no else
found = False
for i in my_list:
    if i == 3:
        print("found")
        found = True
        break
if not found:
    print("not found")

# for loop with else
for i in my_list:
    if i == 3:
        print("found")
        break
else:
    print("not found")
```

* for + else, while + else:
    * break: not run else
    * not break: run else

## 2.5 Variable and Reference 

* a = 1 # name 'a' bound to object 1
* a = 2 # object 1 is not change, name 'a' bound to object 2, id(a) is change
* b = a # id(a) = id(b), name 'b' bound to the same object of 'a'
* Same value might have different id, so do not use "is" for normal value check: 
    * No: if a is 1000,  if a is "hello"
    * Yes: if a == 1000,  if a == "hello", `if a is None`

#### When will python release un-used memory

* Each object has an id, use id(obj) to check
* Each object has a reference count, use sys.getrefcount(obj) to check
* When the reference count of obj reach zero, it will be released at some time for reuse.
    * Add reference: a = "hello"
    * move reference: a = "hello" => a = "world"
    * Remove reference: del a  or return from function, etc.	
    * To explicitly recycle un-used memory: gc.collect()
    
```commandline
>>> a = "hello world"
>>> sys.getrefcount(a)
2
>>> b = a
>>> sys.getrefcount(a),sys.getrefcount(b)
(3, 3)

>>> del b
>>> sys.getrefcount("hello world")
3
>>> sys.getrefcount(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> sys.getrefcount("hello world")
3
>>> gc.collect()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'gc' is not defined
>>> import gc
>>> gc.collect()
0
>>> sys.getrefcount("hello world")
3 # why?
```

## 2.6 Builtin Data Types

#### Frequently used builtin data types

M: Mutable \
H: Hashtable \
C: Container \
I: Iterable \
O: Ordered \
S: Sequence

|Python typical builtin date types|Default value|M|H|C|I|O|S|Note|
|:---|:---|:---|:---|---|---|---|---|---|
||||||||||
||||||||||
|||
|||
|||
|||
|||
|||

## 2.7 Index and slice
## 2.8 Mutable and immutable
## 2.9 str, bytes and bytearray
## 2.10 list and tuple type
## 2.11 dict, OrderedDict and defaultdict
## 2.12 set and frozenset
## 2.13 bool and NoneType
## 2.14 Use "in" operator whenever possible
## 2.15 Function and Parameter type
## 2.16 PEP8 and Python Coding Style Guide
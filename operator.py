Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # arithmetic operator
>>> a=10
>>> b=10
>>> print(a+b)
20
>>> print(a-b)
0
>>> print(a/b)
1.0
>>> # assignment operator
>>> x=20
>>> print(x)
20
>>> #unary minus
>>> a=5
>>> print(a)
5
>>> print(-a)
-5
>>> #relational operators
>>> p=20
>>> q=30
>>> print(p>q)
False
>>> print(p==q)
False
>>> #logical operators
>>> x=true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x=true
NameError: name 'true' is not defined
>>> x=True
>>> y=False
>>> print(x and y)
False
>>> print(x or y)
True
>>> print(not x)
False
>>> #boolean operators
>>> is_pass= True
>>> print (is_pass)
True
>>> #bitwise operators
>>> a=5
>>> b=3
>>> print(a&b)
1
>>> print(a|b)
7
>>> #membership operators
>>> number=[1,2,3,4]
>>> print (2 in numbers)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print (2 in numbers)
NameError: name 'numbers' is not defined
>>> print(2 in number)
True
>>> print (5 not in number)
True
>>> #identity operators
>>> x=10
>>> y=10
>>> print(x is y)
True
>>> print (x is not y)
False
>>> 
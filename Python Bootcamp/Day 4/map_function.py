# -*- coding: utf-8 -*-
"""Map Function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17iHwx83T3xrIR7Ai2TuB4K5Zqh1iHYZB

# Map Function
###### Mapping a Function to an Iterable Object
"""

def cubeNum(num):
  return num**3

a = [1,2,3,4,5]
list(map(cubeNum,a))

"""#Filter Function
Yields Items of Iterale when condition is True
"""

def evenFn(num):
  return num % 2 == 0

a = [0,1,2,3,4,5,6,7,8,9,10]
print(list(filter(evenFn,a)))

"""# Map vs Filter"""

print(list(map(evenFn,a)))
print(list(filter(evenFn,a)))

"""# Lambda Function
Creating Anoynomous Function, without 'def' function
"""

cubefn = lambda num: num**3
cubefn(6)

"""**cubefn** - function name

**num** - arguement name

**num*3** - command to be excecuted when function is called( function body )

**cubefn(6)** - function call

# Args and *kwargs
"""

#Normal Func. with arguements
def addR(a,b,c,d):
  num = a + b + c + d
  return num
addR(10,20,30,40)

#Purpose of Args
def add(*args):        #any number of arguements can be passed
  return(sum(args))
add(10,20,30,40,50,60,70,80,90)

#Purpose of **kwargs
#generates a key-value pair
def func(**kwargs):
  if 'name' in kwargs:
    print("Name is {0}".format(kwargs['name']))
  if 'age' in kwargs:
    print("Age is {0}".format(kwargs['age']))
  else:
    print("No Key Found!")
func(name="Champ",age=24)
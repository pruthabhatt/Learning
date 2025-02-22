# -*- coding: utf-8 -*-
"""Object Oriented Programming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/129x8VyJc6tYmowDnIydMiPK8YJahmZ8R

#Object Oriented Programming

#Class

#Usr Defined Object Created using Class
"""

class Student:
  print("Hello All")
x = Student()   #object instantiation
print(type(x))

"""#Calling Class Function Using Class Name"""

class Student:
  def func():
    print("Welcome to Google Clolab")
Student.func()

"""#"Self" Keyword
A Reference used to access variables of current class.
"""

class Student:
  def func(self):
    print("Self Keyword Demo")
x = Student()
x.func()

class Student:
  year = '2022'
  def func():
    print("Accessing variable using Instance of the Class")
x = Student()
x.year

class Student:
  year = '2022'
  def func(self):
    print("Accessing variable using Instance of the Class",self.year)
x = Student()
x.year

"""#Attribute(Constructor) of An Object using (__init__) method"""

class Student():
  def __init__(self,name):  #method to initialize Attribute(Constructor)
    self.name = name #self.name = attribute initialized
elon = Student(name="Elon Musk") #Creating Instance of Student Class
champ = Student(name="Champion") #Creating Instance of Student Class

print(elon.name) #Accessing Class attribute through instance
print(champ.name)

class Student():
  def __init__(self,name,age):  #method to initialize Attribute(Constructor)
    self.name = name #self.name = attribute initialized
    self.age = age 
elon = Student(name="Elon Musk", age=52) #Creating Instance of Student Class
print(elon.name) #Accessing Class attribute through instance
print(elon.age)

"""#Write a Program to Find out the Difference between Marks Obtained by Students from Total marks --- Using Functions:"""

class Student:
  Total = 500
  def __init__(self,marks):
    self.marks = marks
    print("Initialized....")
  def findLoss(self):
    return self.Total - self.marks
  def findPercentage(self):
    return self.marks/self.Total*100
a = Student(marks=450)
print("Total marks:",a.Total)
print("Marks Obtained:",a.marks)
print("Marks Lost:", a.findLoss())
print("Find Percentage:", a.findPercentage())

"""#Special Methods

"""

class Student:
  total = 500
  def __init__(self,name,marks,gender):
    self.name = name
    self.marks = marks
    self.gender = gender
    print("Initialized")
  def __len__(self):
    return self.marks
  def __str__(self):
    return "Name:%s | Marks:%s | Gender:%s" %(self.name,self.marks,self.gender) 
  def __del__(self):
    print("Student Database is Deleted")
a = Student('Champ',450,'male')
print(a)
print("Marks",len(a))
del a

"""#Inheritance - Helps to Reduce Complexity of Program"""

class Elon:
  def __init__(self):
    print("Profile Created")
  def Name(self):
    print("Elon Musk")
  def Age(self):
    print("45")
class SpaceX(Elon):         #inherited Class. Passing Classname (ELON) as Arguement
  def __init__(self):
    Elon.__init__(self)
    print("Company Profile Created")
  def Name(self):
    print("Name has no Changes")
  def Age(self):
    Elon.Age(self)
    print("Age is Same")
  def Type(self):
    print("Private Space Travel")
a = SpaceX()
a.Name()                  #Derived Class changes the behaviour of the Method
a.Age()

"""#Polymorphism - Different Class Sharing Same Method Names. called from the Same Place but Still shows differently"""

class Elon:
  def __init__(self, name):
    self.name=name
  def type(self):
    return "Enterprenur"
class Sundar:
  def __init__(self,name):
    self.name=name
  def type(self):
    return "CEO"
person1 = Elon("Elon Musk")
person2 = Sundar("Sundar Pichai")

print(person1.type())
print(person2.type())
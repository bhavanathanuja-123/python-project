# class num:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return self.x+other.x,self.y+other.y
# n1=num(10,20)
# n2=num(20,30)
# print(n1+n2)

# class bank:
#     def __init__(self,blc):
#         self.blc=blc
#     def __sub__(self,new):
#         return self.blc-new.blc
# a=bank(1000)
# b=bank(200)
# print(a-b)

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __mul__(self, other):
#         return self.value * other.value
# n1 = Number(10)
# n2 = Number(5)
# print(n1 * n2)

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __floordiv__(self, other):
#         return self.value // other.value
# n1 = Number(10)
# n2 = Number(5)
# print(n1//n2)

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __truediv__(self, other):
#         return self.value /other.value
# n1 = Number(10)
# n2 = Number(5)
# print(n1/n2)

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __mod__(self, other):
#         return self.value // other.value
# n1 = Number(10)
# n2 = Number(5)
# print(n1%n2)

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,others):
#         return self.pages+others.pages
# B1=Book(100)
# B2=Book(200)
# print("Total pages:",B1+B2)

# class Employee:
#     def __init__(self,salary):
#         self.salary=salary
#     def __gt__(self,other):
#         return self.salary>other.salary
# e1=Employee(50000)
# e2=Employee(40000)
# print(e1>e2)

# class Temperature:
#     def __init__(self,temp):
#         self.temp=temp
#     def __sub__(self,other):
#         return self.temp-other.temp
# t1=Temperature(45)
# t2=Temperature(30)
# print("Temperature Difference:",t1-t2)

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def __mul__(self,other):
#         area1=self.length*other.length
#         area2=self.width*other.width
#         return area1*area2
# r1=Rectangle(5,4)
# r2=Rectangle(3,2)
# print("product of areas:",r1*r2)

# class Time:
#     def __init__(self,hours,minutes):
#         self.hours=hours
#         self.minutes=minutes
#     def __add__(self,other):
#         total_hours= self.hours+other.hours
#         total_minutes=self.minutes+other.minutes

#         if total_minutes>=60:
#             total_hours+=total_minutes//60
#             total_minutes=total_minutes%60

#         return Time(total_hours,total_minutes)
#     def display(self):
#        print("Time:",self.hours,"hours",self.minutes,"minutes")

# t1=Time(2,45)
# t2=Time(3,30)
# t3=t1+t2
# t3.display()

# class ShoppingCart:
#     def __init__(self,prices):
#         self.prices=prices
#     def __add__(self,other):
#         return ShoppingCart( self.prices+other.prices)
# cart1=ShoppingCart([100,200,300])
# cart2=ShoppingCart([50,150])
# cart3=cart1+cart2
# print("Combined cart:",cart3.prices)

# class Distance:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x+other.x
#     def __sub__(self,other):
#         return self.x-other.x
#     def __eq__(self,other):
#         return self.x==other.x
# d1=Distance(10)
# d2=Distance(20)
# print(d1+d2)
# print(d1-d2)
# print(d1==d2)

# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
#     def __sub__(self,other):
#         return Vector( self.x-other.x,self.y-other.y)
#     def __mul__(self,other):
#         return (self.x*other.x) +(self.y*other.y)
#     def display(self):
#         print("Vector:",self.x,self.y)
# v1=Vector(3,4)
# v2=Vector(2,5)
# v3=v1+v2
# v3.display()
# v4=v1-v2
# v4.display()
# print("Dot product:",v1 * v2)
# class Animal:
#     def sound(self):
#         print("animal sound")
# class dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class cat(Animal):
#     def sound(self):
#         print("Cat meows")
# class cow(Animal):
#     def sound(self):
#         print("Cow moos")
# animal_sound=[Animal(),dog(),cat(),cow()]
# for i in animal_sound:
#     i.sound()

# class payment:
#     def pay(self):
#         print("payment karoo....")
# class UPI(payment):
#     def pay(self):
#         print("payment through UPI")
# class CreditCard(payment):
#     def pay(self):
#         print("payment through credit card")
# class Cash(payment):
#     def pay(self):
#         print("payment through cash")
# payment_process=[UPI(),CreditCard(),Cash()]
# for i in payment_process:
#     i.pay()

# class Employee:
#     def calculate_salary(self):
#         pass
# class FullTimeEmployee(Employee):
#     def __init__(self,salary):
#         self.salary=salary
#     def calculate_salary(self):
#         return self.salary
# class PartTimeEmployee(Employee):
#     def __init__(self,hours,rate):
#         self.hours=hours
#         self.rate=rate
#     def calculate_salary(self):
#         return self.hours*self.rate
# full_time=FullTimeEmployee(30000)
# part_time=PartTimeEmployee(100,200)

# print("Full-time salary:",full_time.calculate_salary())
# print("part-time salary:",part_time.calculate_salary())
# import math
# class shape:
#     def area(self):
#         print("area of shape")
# class Circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*self.radius*self.radius
# class Rectangle(shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side
# shapes=[Circle(5),Rectangle(10,5),square(4)]
# for shape in shapes:
#     print("Area:",shape.area())

# class Vehicle:
#     def start(self):
#         pass
# class car(Vehicle):
#     def start(self):
#         print("car start with key")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike start with kick")
# class Bus(Vehicle):
#     def start(self):
#         print("Bus start with button")
# vehicle_start=[car(),Bike(),Bus()]
# for i in vehicle_start:
#     i.start()

# class calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# calc=calculator()
# print(calc.add(5,10))
# print(calc.add(10,10,10))
# print(calc.add(20,20,20))

# class EmailNotification:
#     def send(self):
#         print("Sending Email")
# class SMSNotification:
#     def send(self):
#         print("Sending SMS")
# class WhatsAPPNotification:
#     def send(self):
#         print("Sending Whatsapp Message")
# def notify_user(notification):
#     notification.send()
# a=EmailNotification()
# b=SMSNotification()
# c=WhatsAPPNotification()
# notify_user(a)
# notify_user(b)
# notify_user(c)

# class Bank:
#     def interest_rate(self):
#         pass
# class SBI(Bank):
#     def interest_rate(self):
#         return 0.2
# class HDFC(Bank):
#     def interest_rate(self):
#         return 0.5
# class ICICI(Bank):
#     def interest_rate(self):
#         return 7.0
# def display(Bank):
#     print("Interest rate:",Bank.interest_rate(),"%")
# display(SBI())
# display(HDFC())
# display(ICICI())

# class Food:
#     def prepare(self):
#         pass
# class pizza(Food):
#     def prepare(self):
#         print("preparing pizza")
# class Burger(Food):
#     def prepare(self):
#         print("preparing burger")
# class Biryani(Food):
#     def prepare(self):
#         print("preparing biryani")
# def food_list(Food):
#     Food.prepare()
# food_list(pizza())
# food_list(Burger())
# food_list(Biryani())

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
# book1=Book(100)
# book2=Book(200)
# total=book1+book2
# print("Book 1 pages:",book1.pages)
# print("Book 2 pages:",book2.pages)
# print("Total pages:",total)

# class Product:
#     def __init__(self,price):
#         self.price=price
#     def __gt__(self,other):
#         return self.price>other.price
# p1=Product(1000)
# p2=Product(2000)
# if p1>p2:
#     print("product 1 has high price")
# else:
#     print("product 2 has high price")

# class Audio:
#     def play(self):
#         print("Audio playing")
# class Video:
#     def play(self):
#         print("Video playing")
# class Podcast:
#     def play(self):
#         print("Podcast playing")
# def play_media(abc):
#     abc.play()
# play_media(Audio())
# play_media(Video())
# play_media(Podcast())

# class Employee:
#     @classmethod
#     def company_info(cls):
#         print("Employee works in a company")
# class Developer(Employee):
#     @classmethod
#     def company_info(cls):
#         print("Developer works in a software company")
# class DataAnalyst(Employee):
#     @classmethod
#     def company_info(cls):
#         print("Data Analyst works with data")
# Developer.company_info()
# DataAnalyst.company_info()

# class Electronics:
#     def calculate_discount(self, price):
#         discount = price * 0.10
#         return price - discount
# class Clothing:
#     def calculate_discount(self, price):
#         discount = price * 0.20
#         return price - discount
# class Grocery:
#     def calculate_discount(self, price):
#         discount = price * 0.05
#         return price - discount
# def final_price(product, price):
#     print("Final price:", product.calculate_discount(price))

# final_price(Electronics(), 10000)
# final_price(Clothing(), 2000)
# final_price(Grocery(), 1000)

# class Doctor:
#     def treat_patient(self):
#         pass
# class Cardiologist(Doctor):
#     def treat_patient(self):
#         print("Cardiologist treats heart problems")
# class Dentist(Doctor):
#     def treat_patient(self):
#         print("Dentist treats teeth problems")
# class Neurologist(Doctor):
#     def treat_patient(self):
#         print("Neurologist treats nervous system problems")

# doctors = [Cardiologist(),Dentist(),Neurologist()]
# for doctor in doctors:
#     doctor.treat_patient()

# class CSVFile:
#     def read_file(self):
#         print("Reading CSV file")
# class JSONFile:
#     def read_file(self):
#         print("Reading JSON file")
# class TextFile:
#     def read_file(self):
#         print("Reading Text file")
# def process_file(file):
#     file.read_file()

# process_file(CSVFile())
# process_file(JSONFile())
# process_file(TextFile())

# class  Distance:
#     def __init__(self,km,m):
#         self.km=km
#         self.m=m
#     def __add__(self,others):
#         if self.m+others.m>1000:
#             return self.km+others.km,self.m+others.m-1000
#         else:
#              return self.km+others.km,self.m+others.m

# a=Distance(2,500)
# b=Distance(3,800)
# print(a+b)
# 
# class  Distance:
#     def __init__(self,km,m):
#         self.km=km
#         self.m=m
#     def __add__(self,other):
#         total_km=self.km+other.km
#         total_meters=self.m+other.m

#         if total_meters>1000:
#             total_km+total_meters//1000
#             total_meters=total_meters
#         return Distance(total_km,total_meters)
# d1=Distance(2,500)
# d2=Distance(3,800)
# total=d1+d2
# print("total;",total.km,total.m)

# class Employee:
#     def work(self):
#         pass
#     def calculate_bonus(self):
#         pass
#     def display_details(self):
#         pass
# class Manager(Employee):
#     def __init__(self, name):
#         self.name = name
#     def work(self):
#         print(self.name, "manages the team")
#     def calculate_bonus(self):
#         return 10000
#     def display_details(self):
#         print("Manager:", self.name)
# class Developer(Employee):
#     def __init__(self, name):
#         self.name = name
#     def work(self):
#         print(self.name, "develops software")
#     def calculate_bonus(self):
#         return 8000
#     def display_details(self):
#         print("Developer:", self.name)
# class Tester(Employee):
#     def __init__(self, name):
#         self.name = name

#     def work(self):
#         print(self.name, "tests software")

#     def calculate_bonus(self):
#         return 6000

#     def display_details(self):
#         print("Tester:", self.name)
# employees = [Manager("Rahul"),Developer("Priya"),Tester("Arjun")]
# for employee in employees:
#     employee.display_details()
#     employee.work()
#     print("Bonus:", employee.calculate_bonus())
#     print()
# class Ride:
#     def calculate_fare(self,distance):
#         pass
# class BikeRide(Ride):
#     def calculate_fare(self,distance):
#         return distance*10
# class CarRide(Ride):
#     def calculate_fare(self,distance):
#         return distance*20
# class AutoRide(Ride):
#     def calculate_fare(self, distance):
#         return distance*15
# def display_fare(ride,distance):
#     print("Fare:",ride.calculate_fare(distance))
# display_fare(BikeRide(),10)
# display_fare(CarRide(),10)
# display_fare(AutoRide(),10)
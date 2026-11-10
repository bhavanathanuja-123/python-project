# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class student(person):
#     def __init__(self,name,age,course):
#             super().__init__(name,age)
#             self.course=course

#     def display(self):
#             print("Name:",self.name)
#             print("Age:",self.age)
#             print("course:",self.course)

# p1=student("Thanuja",22,"Data science")
# p1.display()

# class Employee:
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department

# class manager(Employee):
#     def __init__(self,name,salary,department,team_size):
#         super(). __init__(name,salary,department)
#         self.team_size=team_size

#     def display(self):
#         print("Name:",self.name)
#         print("Salary:",self.salary)
#         print("Department:",self.department)
#         print("Team_size:",self.team_size)

# e1=manager("Thanuja",50000,"IT",5)
# e1.display()

# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# class car(vehicle):
#     def __init__(self,brand,model,fuel_type):
#         super().__init__(brand,model)
#         self.fuel_type=fuel_type
#     def display(self):
#         print("Brand:",self.brand)
#         print("Model:",self.model)
#         print("Fuel_type:",self.fuel_type)

# c1=car("Toyota","Fortuner","Diesel")
# c1.display()

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
# class SavingsAccount(BankAccount):
#     def __init__(self,account_number,balance,interest_rate):
#         super().__init__(account_number,balance)
#         self.interest_rate=interest_rate
#     def display(self):
#         print("Account Number:",self.account_number)
#         print("Balance:",self.balance)
#         print("Interest rate:",self.interest_rate)
# s1=SavingsAccount(12344,40000,0.20)
# s1.display()

# class Product:
#     def __init__(self, product_name, price):
#         self.product_name = product_name
#         self.price = price


# class ElectronicProduct(Product):
#     def __init__(self, product_name, price, warranty_years):
#         super().__init__(product_name, price)
#         self.warranty_years = warranty_years

#     def display(self):
#         print("Product:", self.product_name)
#         print("Price:", self.price)
#         print("Warranty:", self.warranty_years, "years")


# p = ElectronicProduct("Laptop", 50000, 2)
# p.display()

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Breed:", self.breed)


# d = Dog("Tommy", 3, "Labrador")
# d.display()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class student(person):
#     def __init__(self,name,age,course,marks):
#         super().__init__(name,age)
#         self.course=course
#         self.marks=marks
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)
#         print("Marks:",self.marks)
# s1=student("Anu",25,"python",80)
# s1.display()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Developer(Employee):
#     def __init__(self, name, salary, language, experience):
#         super().__init__(name, salary)
#         self.language = language
#         self.experience = experience

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Language:", self.language)
#         print("Experience:", self.experience)


# d1=Developer("Anusha", 60000, "Python", 2)
# d1.display()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, fuel_type, price):
#         super().__init__(brand, model)
#         self.fuel_type = fuel_type
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Fuel Type:", self.fuel_type)
#         print("Price:", self.price)

# c = Car("Honda", "City", "Petrol", 1200000)
# c.display()

# class BankAccount:
#     def __init__(self, holder_name, balance):
#         self.holder_name = holder_name
#         self.balance = balance

# class SavingsAccount(BankAccount):
#     def __init__(self, holder_name, balance, interest_rate):
#         super().__init__(holder_name, balance)
#         self.interest_rate = interest_rate

#     def calculate_balance(self):
#         interest = self.balance * self.interest_rate / 100
#         final_balance = self.balance + interest
#         print("Holder:", self.holder_name)
#         print("Initial Balance:", self.balance)
#         print("Interest:", interest)
#         print("Final Balance:", final_balance)

# s1 = SavingsAccount("Thanuja", 10000, 5)
# s1.calculate_balance()

# class Company:
#     def __init__(self, company_name):
#         self.company_name = company_name

# class Employee(Company):
#     def __init__(self, company_name, employee_name, salary):
#         super().__init__(company_name)
#         self.employee_name = employee_name
#         self.salary = salary

#     def display(self):
#         print("Company:", self.company_name)
#         print("Employee:", self.employee_name)
#         print("Salary:", self.salary)

# e1 = Employee("TCS", "Priya", 45000)
# e1.display()

# class person:
#     def __init__(self,name):
#         self.name=name

# class Employee(person):
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary=salary
# class manager(Employee):
#     def __init__(self,name,salary,team_size):
#         super().__init__(name,salary)
#         self.team_size=team_size
#     def display(self):
#         print("Name:",self.name)
#         print("Salary:",self.salary)
#         print("Team size;",self.team_size)

# m1=manager("keerthi",50000,4)
# m1.display()

# class student:
#     def __init__(self,name):
#         self.name=name
# class GraduateStudent(student):
#     def __init__(self,name,degree):
#         super().__init__(name)
#         self.degree=degree
# class ReasearchStudent(GraduateStudent):
#     def __init__(self,name,degree,topic):
#         super().__init__(name,degree)
#         self.topic=topic
#     def display(self):
#         print("Name:",self.name)
#         print("Degree:",self.degree)
#         print("Reasearch Topic:",self.topic)

# r=ReasearchStudent("Thanuja","M.Tech","Artifical Intelligence")
# r.display()

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(self.name,"eats food")
# class Mammal(Animal):
#     def walk(self):
#         print(self.name,"can walk")
# class Dog(Mammal):
#     def bark(self):
#         print(self.name,"barks")
# d=Dog("Tommy")
# print("Name:",d.name)
# d.eat()
# d.walk()
# d.bark()

# class Father:
#     def home(self):
#         print("father have home")
# class Mother:
#     def gold(self):
#         print("mother have 200gms gold")
# class child(Father,Mother):
#     def bike(self):
#         print("son have bike")
# a=child()
# a.home()
# a.gold()
# a.bike()

# class Printer:
#     def print(self):
#         print("printing document")
# class Scanner:
#     def scan(self):
#         print("scanning document")
# class Machine(Printer,Scanner):
#     pass
# m=Machine()
# m.print()
# m.scan()

# class Teacher:
#     def teach(self):
#         print("professor teaches student")
# class Researcher:
#     def research(self):
#         print("professor does research")
# class Professor(Teacher,Researcher):
#     pass
# p1=Professor()
# p1.teach()
# p1.research()

# class Developer:
#     def develop(self):
#         print("developing application")
# class Designer:
#     def design(self):
#         print("Designing user interface")
# class UIDeveloper(Developer,Designer):
#     pass
# u1=UIDeveloper()
# u1.develop()
# u1.design()

# class Employee:
#     def company(self):
#         print("employee working in wipro")
# class Developer(Employee):
#     def work(self):
#         print("developer write a code")
# class Tester(Employee):
#     def test(self):
#         print("Test the code")
# a=Tester()
# a.company()
# a.test()

# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def bark(self):
#         print(self.name,"barks")
# class Cat(Animal):
#     def meow(self):
#         print(self.name,"meows")
# class Cow(Animal):
#     def sound(self):
#         print(self.name,"moos")
# d=Dog("Tommy")
# d.bark()
# c=Cat("kitty")
# c.meow()
# w=Cow("Ganga")
# w.sound()

# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
# class Car(Vehicle):
#     def display(self):
#            print("Car Brand:", self.brand)
# class Bike(Vehicle):
#     def display(self):
#         print("Bike Brand:", self.brand)
# class Bus(Vehicle):
#     def display(self):
#         print("Bus Brand:", self.brand)
# c = Car("Toyota")
# c.display()
# b = Bike("Honda")
# b.display()
# bus = Bus("Volvo")
# bus.display()

# class Employee:
#     def __init__(self,name):
#         self.name=name
#     def display_employee(self):
#         print("Employee:",self.name)
# class Developer(Employee):
#     def develop(self):
#         print("Developer develops software")
# class Tester(Employee):
#     def test(self):
#         print("Tester tests software")
# class TeamLead(Developer,Tester):
#     def lead(self):
#         print("Team lead manages the team")
# t=TeamLead("Thanuja")
# t.display_employee()
# t.develop()
# t.test()
# t.lead()

# class Device:
#     def __init__(self,brand):
#         self.brand=brand
#     def display_device(self):
#         print("Brand:",self.brand)
# class phone(Device):
#     def call(self):
#         print("phone can make calls")
# class camera(Device):
#     def take_photo(self):
#         print("camera can take photos")
# class smartphone(phone,camera):
#     def display(self):
#         print("smartphone:",self.brand)
# s=smartphone("samsung")
# s.display()
# s.take_photo()
# s.call()

# class Person:
#     def __init__(self, name):
#         self.name = name
# class Student(Person):
#     def __init__(self, name, course):
#         Person.__init__(self, name)
#         self.course = course
# class Employee(Person):
#     def __init__(self, name, salary):
#         Person.__init__(self, name)
#         self.salary = salary
# class Intern(Student, Employee):
#     def __init__(self, name, course, salary, duration):
#         Student.__init__(self, name, course)
#         Employee.__init__(self, name, salary)
#         self.duration = duration
#     def display(self):
#         print("Name:", self.name)
#         print("Course:", self.course)
#         print("Salary:", self.salary)
#         print("Duration:", self.duration)
# i = Intern("Thanuja", "Python", 20000, "6 months")
# i.display()

# class Library:
#         def __init__(self, library_name):
#            self.library_name = library_name
# class Book(Library):
#     def __init__(self, library_name, title, author, price):
#         super().__init__(library_name)
#         self.title = title
#         self.author = author
#         self.price = price
# class EBook(Book):
#     def __init__(self, library_name, title, author, price, file_size):
#         super().__init__(library_name, title, author, price)
#         self.file_size = file_size
#     def display(self):
#         print("Library:", self.library_name)
#         print("Book:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)
#         print("File Size:", self.file_size, "MB")
# e = EBook("City Library", "Python Basics","John", 500, 25)
# e.display()

# class User:
#     def __init__(self, username):
#         self.username = username
# class Customer(User):
#     def __init__(self, username, address):
#         User.__init__(self, username)
#         self.address = address
# class Seller(User):
#     def __init__(self, username, shop_name):
#         User.__init__(self, username)
#         self.shop_name = shop_name
# class Marketplace(Customer, Seller):
#     def __init__(self, username, address, shop_name):
#         Customer.__init__(self, username, address)
#         Seller.__init__(self, username, shop_name)
#     def display(self):
#         print("Username:", self.username)
#         print("Address:", self.address)
#         print("Shop Name:", self.shop_name)
# class Assistant(Student, Teacher):
#  = Marketplace("Rahul", "Hyderabad", "RahulElectronics")
# m.display()

# class Person:
#     def __init__(self, name):
#         self.name = name
# class Student(Person):
#     def __init__(self, name, course):
#         Person.__init__(self, name)
#         self.course = course
# class Teacher(Person):
#     def __init__(self, name, subject):
#         Person.__init__(self, name)
#         self.subject = subject
# class Assistant(Student, Teacher):
#     def __init__(self, name, course, subject):
#         Student.__init__(self, name, course)
#         Teacher.__init__(self, name, subject)
#     def display(self):
#         print("Name:", self.name)
#         print("Course:", self.course)
#         print("Subject:", self.subject)
# a = Assistant("Bhavana", "B.Tech", "Python")
# a.display()

# class Account:
#     def __init__(self, holder_name, account_number, balance):
#         self.holder_name = holder_name
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Deposited:", amount)

#     def withdrawal(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def display(self):
#         print("Account Holder:", self.holder_name)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
# class Savings(Account):
#     pass
# class Current(Account):
#     pass
# s = Savings("Bhavana", 101, 10000)
# s.display()
# s.deposit(2000)
# s.withdrawal(3000)
# print("After transactions:")
# s.display()
# # Current account
# c = Current("Rahul", 102, 20000)
# c.display()
# c.deposit(5000)
# c.withdrawal(4000)
# print("After transactions:")
# c.display()
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_employee(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         Employee.__init__(self, name, salary)
#         self.language = language

#     def develop(self):
#         print("Programming Language:", self.language)
# class Tester(Employee):
#     def __init__(self, name, salary, tool):
#         Employee.__init__(self, name, salary)
#         self.tool = tool

#     def test(self):
#         print("Testing Tool:", self.tool)
# class TeamLead(Developer, Tester):
#     def __init__(self, name, salary, language, tool):
#         Developer.__init__(self, name, salary, language)
#         Tester.__init__(self, name, salary, tool)

#     def lead(self):
#         print("Team Lead manages the team")
# t = TeamLead("Thanuja", 70000, "Python", "Selenium")
# t.display_employee()
# t.develop()
# t.test()
# t.lead()

class student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)

# s1=student("Thanuja",22,"Datascience")
# s1.display()

# class employee:
#     def __init__(self,name,basic_salary):
#         self.name=name
#         self.basic_salary=basic_salary
#     def display(self):
#         print("Name:",self.name)
#         print("basic_salary:",self.basic_salary)
# e1=employee("Thanuja",20000)
# e1.display()

# class mobilephone:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def display(self):
#         print("Brand:",self.brand)
#         print("Model:",self.model)
#         print("Price:",self.price)

# m1=mobilephone("samsung","A55",30000)
# m2=mobilephone("Apple","iphone 15",60000)
# m3=mobilephone("Oneplus","12R",40000)

# m1.display()
# m2.display()
# m3.display()

# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         print("Area:",self.length*self.breadth)
#     def permiter(self):
#         print("perimeter:",2*(self.length+self.breadth))
# r1=rectangle(10,5)
# r1.area()
# r1.permiter()

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display_marks(self):
#         print("Name:",self.name)
#         print("marks:",self.marks)
#     def check_result(self):
#         if self.marks>=40:
#             print("Result:pass")
#         else:
#             print("Result:Fail")

# s1=student("Thanuja",80)
# s1.display_marks()
# s1.check_result()
# s2=student("Keerthi",85)
# s2.display_marks()
# s2.check_result()
# s3=student("Vijaya",30)
# s3.display_marks()
# s3.check_result()
# s4=student("Naga",28)
# s4.display_marks()
# s4.check_result()
# s5=student("Shafiya",35)
# s5.display_marks()
# s5.check_result()

# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def calculate_bonus(self):
#         if self.salary>=50000:
#             bonus=self.salary*0.10
#         else:
#             bonus=self.salary*0.05
#         total=self.salary+bonus

#         print("Employee Name:",self.name)
#         print("Salary:",self.salary)
#         print("Bonus:",bonus)
#         print("Total Salary:",total)

# e1=employee("Thanuja",50000)
# e2=employee("Keerthi",40000)
# e1.calculate_bonus()
# e2.calculate_bonus()

# class product:
#     def __init__(self,product_name,price):
#         self.product_name=product_name
#         self.price=price

#     def calculate_discount(self):
#         if self.price>=5000:
#             discount=self.price*0.20
#         elif self.price>=2000:
#             discount=self.price*0.10
#         else:
#             discount=self.price*0.05

#         final_price=self.price-discount

#         print("Product:",self.product_name)
#         print("Original price:",self.price)
#         print("Discount:",discount)
#         print("Final price:",final_price)

# p1=product("Laptop",50000)
# p2=product("Head phones",3000)
# p3=product("Mouse",1000)

# p1.calculate_discount()
# p2.calculate_discount()
# p3.calculate_discount()

# class ATM:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("Depoisted:",amount)
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient  Balance")
#         else:
#             self.balance=self.balance-amount
#             print("Withdrawn:",amount)

#     def check_balance(self):
#         print("Current Balance:",self.balance)

# a1=ATM(12345,10000)
# a1.check_balance()
# a1.deposit(5000)
# a1.check_balance()
# a1.withdraw(3000)
# a1.check_balance()

# class Car:
#     def __init__(self, brand, model, price, fuel_type):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.fuel_type = fuel_type

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
#         print("Fuel Type:", self.fuel_type)

#     def check_price(self):
#         if self.price > 1000000:
#             print("Premium Car")
#         else:
#             print("Normal Car")


# c1 = Car("Toyota", "Fortuner", 3500000, "Diesel")

# c1.display()
# c1.check_price()

# class ElectricityBill:
#     def __init__(self, customer_name, units):
#         self.customer_name = customer_name
#         self.units = units

#     def calculate_bill(self):
#         if self.units <= 100:
#             bill = self.units * 2
#         elif self.units <= 200:
#             bill = self.units * 3
#         elif self.units <= 300:
#             bill = self.units * 5
#         else:
#             bill = self.units * 7

#         return bill

#     def display_bill(self):
#         bill = self.calculate_bill()

#         print("Customer Name:", self.customer_name)
#         print("Units:", self.units)
#         print("Bill:", bill)


# e1 = ElectricityBill("Thanuja",150)
# e1.display_bill()

# class Book:
#     def __init__(self,title,author,price,available):
#         self.title=title
#         self.author=author
#         self.price=price
#         self.available=available
#     def display_book(self):
#         print("Title:",self.title)
#         print("Autor:",self.author)
#         print("Price:",self.price)
#         print("Available:",self.available)

#     def borrow_book(self):
#         if self.available:
#             print("Book borrowed successfully")
#         else:
#             print("Book is not available")

#     def return_book(self):
#         self.available=True
#         print("Book returned successfully")
# b1=Book("Python basics","nani",500,True)
# b1.display_book()
# b1.borrow_book()
# b1.return_book()

# class product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def calculate_total(self):
#         return self.price*self.quantity
#     def display_product(self):
#         print("Product:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total:", self.calculate_total())

# p1=product("Laptop",50000,1)
# p2=product("Mouse",1000,2)
# p3=product("Keyboard",2000,1)

# p1.display_product()
# p2.display_product()
# p3.display_product()

# total = p1.calculate_total() + p2.calculate_total() + p3.calculate_total()

# print("Total Shopping Amount:", total)

# class Employee:
#     def __init__(self, name, salary, rating):
#         self.name = name
#         self.salary = salary
#         self.rating = rating

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Rating:", self.rating)

#     def calculate_increment(self):
#         if self.rating >= 4.5:
#             increment = self.salary * 0.20
#         elif self.rating >= 3.5:
#             increment = self.salary * 0.10
#         else:
#             increment = self.salary * 0.05

#         new_salary = self.salary + increment

#         print("Increment:", increment)
#         print("New Salary:", new_salary)


# e1 = Employee("Thanuja", 50000, 4.7)

# e1.display()
# e1.calculate_increment()

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if self.balance - amount < 1000:
#             print("Withdrawal not allowed")
#             print("Minimum balance of ₹1000 must be maintained")
#         else:
#             self.balance = self.balance - amount
#             print("Withdrawn:", amount)

#     def check_balance(self):
#         print("Balance:", self.balance)


# b1 = BankAccount("Thanuja", 5000)

# b1.check_balance()
# b1.withdraw(3000)
# b1.check_balance()

# b1.withdraw(1500)
# b1.check_balance()

# class foodorder:
#     def __init__(self,customer_name,food_name,price,quantity):
#         self.customer_name=customer_name
#         self.food_name=food_name
#         self.price=price
#         self.quantity=quantity

#     def calculate_total(self):
#         return self.price*self.quantity
#     def apply_discount(self):
#         total=self.calculate_total()

#         if total>=2000:
#             discount=total*0.20
#         elif total >=1000:
#             discount=total*0.10
#         else:
#             discount=0

#         final_price=total-discount
#         return discount,final_price
#     def display_order(self):
#         total=self.calculate_total()
#         discount,final_price=self.apply_discount()

#         print("Customer:",self.customer_name)
#         print("Food:",self.food_name)
#         print("Total:",total)
#         print("Discount:",discount)
#         print("Final price:",final_price)

# f1=foodorder("Thanuja","Biryani",500,5)
# f1.display_order()

# class Patient:
#     def __init__(self, name, age, disease, bill):
#         self.name = name
#         self.age = age
#         self.disease = disease
#         self.bill = bill

#     def display_patient(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Disease:", self.disease)
#         print("Bill:", self.bill)

#     def add_bill(self, amount):
#         self.bill = self.bill + amount

#     def check_bill(self):
#         print("Current Bill:", self.bill)


# p1 = Patient("Rahul", 25, "Fever", 2000)
# p2 = Patient("Priya", 30, "Cold", 1500)

# p1.add_bill(1000)
# p2.add_bill(500)

# p1.display_patient()
# p1.check_bill()
# p2.display_patient()
# p2.check_bill()

# class Employee:
#     def __init__(self, name, total_days, present_days):
#         self.name = name
#         self.total_days = total_days
#         self.present_days = present_days

#     def attendance_percentage(self):
#         return (self.present_days / self.total_days) * 100

#     def check_attendance(self):
#         percentage = self.attendance_percentage()

#         print("Employee:", self.name)
#         print("Attendance:", percentage, "%")

#         if percentage >= 75:
#             print("Eligible")
#         else:
#             print("Not Eligible")


# e1 = Employee("Rahul", 100, 80)
# e2 = Employee("Priya", 100, 60)

# e1.check_attendance()
# e2.check_attendance()

# class MovieTicket:
#     def __init__(self, movie_name, ticket_price, number_of_tickets):
#         self.movie_name = movie_name
#         self.ticket_price = ticket_price
#         self.number_of_tickets = number_of_tickets

#     def calculate_total(self):
#         return self.ticket_price * self.number_of_tickets

#     def apply_discount(self):
#         total = self.calculate_total()

#         if self.number_of_tickets >= 5:
#             discount = total * 0.10
#         else:
#             discount = 0

#         return discount, total - discount

#     def display_ticket(self):
#         total = self.calculate_total()
#         discount, final_price = self.apply_discount()

#         print("Movie:", self.movie_name)
#         print("Ticket Price:", self.ticket_price)
#         print("Number of Tickets:", self.number_of_tickets)
#         print("Total:", total)
#         print("Discount:", discount)
#         print("Final Price:", final_price)


# m1 = MovieTicket("Avatar", 250, 6)

# m1.display_ticket()

# class student:
#     def __init__(self,name,roll_no,python,sql,powerbi):
#         self.name=name
#         self.roll_no=roll_no
#         self.python=python
#         self.sql=sql
#         self.powerbi=powerbi

#     def calculate_total(self):
#         return self.python + self.sql + self.powerbi

#     def calculate_average(self):
#         total = self.calculate_total()
#         return total / 3

#     def calculate_grade(self):
#         average = self.calculate_average()

#         if average >= 90:
#             return "A"
#         elif average >= 75:
#             return "B"
#         elif average >= 60:
#             return "C"
#         elif average >= 40:
#             return "D"
#         else:
#             return "Fail"

#     def display_report(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Python:", self.python)
#         print("SQL:", self.sql)
#         print("PowerBI:", self.powerbi)
#         print("Total:", self.calculate_total())
#         print("Average:", self.calculate_average())
#         print("Grade:", self.calculate_grade())


# s1=student("Thanuja", 101, 85, 90, 80)
# s1.display_report()


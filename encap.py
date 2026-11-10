# class student:
#     def __init__(self,name):
#         self.name=name
# a=student("Thanuja")
# print(a.name)

# class  student:
#     def __init__(self,name):
#         self._name=name
# s=student("Thanuja")
# print(s._name)

# class student:
#     def __init__(self,name):
#         self.__name=name
#     def display(self):
#         print(self.__name)
# s=student("Thanuja")
# s.display()

# class student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         self.__marks=marks
# s=student(80)
# print(s.get_marks())
# s.set_marks(90)
# print(s.get_marks())

# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def get_balance(self):
#         return self.__balance
# account=bankaccount(5000)
# account.deposit(2000)
# print(account.get_balance())

# class number:
#     def __init__(self):
#         self.n=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n<=10:
#             var=self.n
#             self.n+=1
#             return var
#         else:
#             raise StopIteration
        
# a=number()
# for i in a:
#     print(i)

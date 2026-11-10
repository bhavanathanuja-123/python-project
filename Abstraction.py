# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         print("payment process")
# class upi(payment):
#     def pay(self,amt):
#         print("paid",amt,"with upi")
# class cash(payment):
#     def pay(self,amt):
#         print("paid",amt,"with cash")
# a=upi()
# a.pay(500)
# b=cash()
# b.pay(200)

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     def stop(self):
#         print("stop the vehicle")
# class car(Vehicle):
#     def start(self):
#         print("car start with key")
# class bike(Vehicle):
#     def start(self):
#         print("bike start with self btn")
# a=car()
# a.start()
# a.stop()
# b=bike()
# b.start()
# b.stop()

# class food_order:
#     def place_order(self):
#         self._payment_method()
#         self._res_note()
#         print("order done")
#     def _payment_method(self):
#         print("payment process (upi,cash,cod,card)")
#     def _res_note(self):
#         print("rest_info...")
# c=food_order()
# c.place_order()

# from abc import ABC,abstractmethod
# class msg(ABC):
#     @abstractmethod
#     def send(self):
#         print("send a msg")
# class sms(msg):
#     def send(self):
#         print("sms msg")
# class email(msg):
#     def send(self):
#         print("email msg")
# def send_msg(a):
#     a.send()
# p=sms()
# send_msg(p)
# p1=email()
# send_msg(p1)

# from abc import ABC,abstractmethod

# import pyttsx3 as pt
# import random as dm
# from datetime import datetime as dt
# import mysql.connector
# e=pt.init()

# con=mysql.connector.connect(
#      host="localhost",
#      user="root",
#      password="Bhavana22@",
#      db="bank_db",
# )
# cos=con.cursor()

# class payment(ABC):
#     @abstractmethod
#     def pay(self,amt):
#         pass 
# def save_transaction(id,method,amount,date):
#          query="insert into transaction(transaction_id, payment_method,amount,transaction_date) values(%s,%s,%s,%s)"
#          values=(id,method,amount,date)
#          cos.execute(query,values)
#          con.commit()
#          cos.close()
#          print("Transaction saved successfully!")
# class phonepay(payment):
#     def pay(self,amt):
#         self.amt=amt
#         msg=str(amt)+"rupees received by phonepay thank you boss"
#         e.say(msg)
#         e.runAndWait()
#         transaction_id=dm.randint(100000,999999)
#         transaction_date=dt.today()
#         print(".......transaction details........")
#         print("transaction id:=",transaction_id)
#         print("transaction date:=",transaction_date)
#         save_transaction(transaction_id,"phonepay",amt,transaction_date)

# class gpay(payment):
#      def pay(self,amt):
#             self.amt=amt
#             msg=str(amt)+"rupees received by gpay thank you boss"
#             e.say(msg)
#             e.runAndWait()
#             transaction_id=dm.randint(100000,999999)
#             transaction_date=dt.today()
#             print(".......transaction details........")
#             print("transaction id:=",transaction_id)
#             print("transaction date:=",transaction_date)
#             save_transaction(transaction_id,"gpay",amt,transaction_date)

# class pytm(payment):
#       def pay(self,amt):
#              self.amt=amt
#              msg=str(amt)+"rupees received by pytm thank you boss"
#              e.say(msg)
#              e.runAndWait()
#              transaction_id=dm.randint(100000,999999)
#              transaction_date=dt.today()
#              print(".......transaction details........")
#              print("transaction id:=",transaction_id)
#              print("transaction date:=",transaction_date)
#              save_transaction(transaction_id,"pytm",amt,transaction_date)

# class other(payment):
#       def pay(self,amt):
#              self.amt=amt
#              msg=str(amt)+"rupees received by others thank you boss"
#              e.say(msg)
#              e.runAndWait()
#              transaction_id=dm.randint(100000,999999)
#              transaction_date=dt.today()
#              print(".......transaction details........")
#              print("transaction id:=",transaction_id)
#              print("transaction date:=",transaction_date)
#              save_transaction(transaction_id,"other",amt,transaction_date)

# choose=int(input("enter number 1.phonepay,2.gpay,3.pytm,4.other"))
# amount=int(input("enter the amount:"))

# if choose==1:
#      app=phonepay()
# elif choose==2:
#      app=gpay()
# elif choose==3:
#      app=pytm()
# elif choose==4:
#      app=other()
# else:
#      print("Invalid app")

# app.pay(amount)





from abc import ABC,abstractmethod
import mysql.connector as mysql
import pyttsx3 as pt
import random as dm
from datetime import datetime as dt

e=pt.init()

con=mysql.connect(
    host="localhost",
    user="root",
    password="Bhavana22@",
    db="payment_db"

)

class payment(ABC):
    @abstractmethod
    def pay(self,amt):
        pass
    def save_transaction(self,app_name,amt):
        cursor=None
        try:
            cursor=con.cursor()
            transaction_id=dm.randint(100000,999999)
            transaction_date=dt.now()

            query="insert into transaction (transaction_id,payment_app,amount,transaction_date) values (%s,%s,%s,%s)"
            values=(
                transaction_id,
                app_name,
                amt,
                transaction_date
            )

            cursor.execute(query,values)
            con.commit()
        except mysql.Error as err:
            print("mysql error",err )
            con.rollback()

        finally:
            if cursor is not None:
                cursor.close()
class phonepay(payment):
    def pay(self,amt):
        self.amt=amt
        msg=str(amt)+"rupees recived by phonepay thank you boss"
        e.say(msg)
        e.runAndWait()
        self.save_transaction("phone_pay",amt)

class gpay(payment):
    def pay(self,amt):
        self.amt=amt
        msg=str(amt)+"rupees recived by gpay thank you boss"
        e.say(msg)
        e.runAndWait()
        self.save_transaction("gpay",amt)

class other(payment):
    def pay(self,amt):
        self.amt=amt
        msg=str(amt)+"rupees recived by other thank you boss"
        e.say(msg)
        e.runAndWait()
        self.save_transaction("other",amt)
try:
    c=int(input("enter 1.phonepay,2.gpay,3.other: ="))
    if c not in (1,2,3):
        print("invalid app")
    else:
        amt=int(input("enter amount := "))
        if amt<0:
            print("invalid amt")
        else:
            if c==1:
                app=phonepay()
            elif c==2:
                app=gpay()
            elif c==3:
                app=other()
            else:
                print("invalid")
            app.pay(amt)

finally:
    if con is not None and con.is_connected():
        con.close()
        print("database connection closed")

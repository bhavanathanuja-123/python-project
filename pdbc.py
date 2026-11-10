# from mysql.connector import connect

# con = connect(
#     host="localhost",
#     user="root",
#     password="Bhavana22@",
#     db="da"

# )

# cos=con.cursor()
# cos.execute("select *from employees")

# for i in cos.fetchone():
#        print(i)

from mysql.connector import connect

con=connect(
    host="localhost",
    user="root",
    password="Bhavana22@",
    db="da"

)
cos=con.cursor()
query="update  cust set cust_name=%s where cust_id=%s"
values=("Thanuja",5)
cos.execute(query,values)
con.commit()
cos.execute("select*from cust")
for i in cos.fetchall():
    print(i)

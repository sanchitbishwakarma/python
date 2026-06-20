import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="company_db"
)

cur = con.cursor()

cur.execute(
    "INSERT INTO customer (cid, name, age, address, salary) VALUES (100, 'Harii', 20, 'Nepal', 100)"
)

cur.execute(
    "DELETE FROM customer WHERE customer.cid = 1"
)


cur.execute(
    "SELECT * FROM deleted_customer"
)

res = cur.fetchall()
for row in res:
    print(row)

con.commit()
con.close()
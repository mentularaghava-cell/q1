import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
with conn:
    c.execute(""" CREATE TABLE employees(
        id INTEGER PRIMARY KEY,
        first TEXT NOT NULL,
        last TEXT NOT NULL,
        pay INTEGER)
 """)

with conn:
    c.execute("INSERT INTO employees (first,last,pay) VALUES(?,?,?)",("Rohan","Sharma",100000))
    c.execute("INSERT INTO employees (first,last,pay) VALUES(?,?,?)",("Ravi","Kumar",80000))
    c.execute("INSERT INTO employees (first,last,pay) VALUES(?,?,?)",("Kiran","Rao",90000))
with conn:
    c.execute("SELECT COUNT(*) FROM employees")
    print(c.fetchall())

with conn:
    c.execute("SELECT FIRST,LAST,PAY FROM employees WHERE pay > ?",(85000,))
    print(c.fetchall())
with conn:#SELECT -> FROM -> ORDER BY -> ASC(assending) or DESC(decending)
    c.execute("SELECT first,last,pay FROM employees  ORDER BY pay DESC")
    print(c.fetchall())
with conn:
    c.execute("SELECT MAX(pay) FROM employees WHERE pay !=(SELECT MAX(pay) FROM employees)")
def fillter_employees():
    with conn:
        c.execute("SELECT first,last,pay FROM employees WHERE((pay > ?) AND ((pay > ?) OR (first = 'Raghava'))) ORDER BY pay DESC",(50000,90000))
        print(c.fetchall())
with conn:
    c.execute("SELECT COUNT(*) FROM employees WHERE pay > ?",(70000,))
    c.execute("SELECT AVG(pay) FROM employees WHERE pay > ?",(50000,))

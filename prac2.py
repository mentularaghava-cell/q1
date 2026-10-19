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

def dis():
    with conn:
        c.execute("SELECT * FROM employees")
        print(c.fetchall())

def insert(first,last,pay):
    with conn:
        c.execute("INSERT INTO employees  (first,last,pay) VALUES(:first,:last,:pay)",{"first":first,"last":last,"pay":pay})

def update(first,last,pay):
    with conn:
        c.execute("UPDATE employees SET pay=:pay WHERE last=:last AND first=:first",{"first":first,"last":last,"pay":pay})
    print(c.rowcount)

def delete(first,last):
    with conn:
        c.execute("DELETE FROM employees  WHERE last=:last AND first=:first",{"first":first,"last":last})
    print(c.rowcount)

def max():
    with conn:
        c.execute("SELECT MAX(pay) from employees")
    return c.fetchone()

def min():
    with conn:
        c.execute("SELECT MIN(pay) from employees")
    return c.fetchone()

def avg():
    with conn:
        c.execute("SELECT AVG(pay) from employees")
    return c.fetchone()


dis()
insert("Krish","Hari",200000)
update("Krish","Hari",300000)
delete("Ravi","Kumar")
dis()

with conn:
    c.execute("SELECT first,last,pay FROM employees WHERE pay = (SELECT MAX(pay) FROM employees)")
    print(c.fetchone())
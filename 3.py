import sqlite3
from employee import Employee

conn = sqlite3.connect(":memory:")#no real file is created (if u use':memory:')it is stored in RAM

c = conn.cursor()
query= """CREATE TABLE employees(
        first TEXT,
        last TEXT,
        pay INTEGER)"""
c.execute(query)

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees  VALUES(:first,:last,:pay)",{"first":emp.first,"last":emp.last})
        return c.fetchall()
        
def get_emp_by_name(lastname):
    with conn:
        c.execute("SEARCH * FROM employees WHERE last=:last",{'last':lastname})
        return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("UPDATE employees SET pay=:pay WHERE first=:first AND last=:last",{"first":emp.first,"last":emp.last,"pay":pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first=:first AND last = :last",{"first":emp.first,"last":emp.last})

emp_1 = Employee("Jonh","Deo",80000)
emp_2 = Employee("Scena","Oho",90000)
#tuple
with conn:#if we use with we don't need to use commit
    c.execute("INSERT INTO employees VALUES (? ,? ,?)",(emp_1.first,emp_1.last,emp_1.pay))

#another methode to give parameters
c.execute("INSERT INTO employees VALUES ( :first, :last, :pay)",{"first":emp_2.first,"last":emp_2.last,"pay":emp_2.pay})
conn.commit()
# % — matches any sequence of characters. ex: %food fastfood,food
# — matches exactly one character.ex: c_t     cat,cut 

c.execute("SELECT * FROM employees WHERE last=?",("Deo",))
conn.commit()
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last",{"last":"Oho"})
conn.commit()

print(c.fetchall())


conn.close()
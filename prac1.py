import sqlite3

conn = sqlite3.connect("company.db")

c = conn.cursor()
c.execute("""
        CREATE TABLE IF NOT EXISTS  employees (
            id  INTEGER PRIMARY KEY,
            first TEXT,
            last TEXT,
            pay INTEGER)

""")
conn.commit()

with conn:
    c.execute("INSERT INTO employees (first,last,pay) VALUES(?,?,?)",("Rohan","Sharma",100000))
    c.execute("INSERT INTO employees (first,last,pay) VALUES(?,?,?)",("Ravi","Kumar",80000))
    c.execute("INSERT INTO employees (first,last,pay) VALUES(?,?,?)",("Kiran","Rao",90000))
with conn:
    c.execute("SELECT * FROM employees")
print(c.fetchall())

with conn:
    c.execute("UPDATE employees  SET PAY=:pay WHERE first=:first AND last=:last",{"first":"Rohan","last":"Kumar","pay":100000})
with conn:
    c.execute("SELECT * FROM employees")
print(c.fetchall())


with conn:
    c.execute("DELETE FROM employees WHERE first=:first AND last=:last",{"first":"Kiran","last":"Rao"})

with conn:
    c.execute("SELECT * FROM employees")
print(c.fetchall())


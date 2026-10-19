import sqlite3
from icecream import ic as print

#establising a database
connection = sqlite3.connect("Raghava.db")#make a database
cursor = connection.cursor()#interact with dattabase
# cursor.execute()#we write our sql queries
connection.close()

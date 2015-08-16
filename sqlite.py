__author__ = 'Prudhvi'

import sqlite3

db = sqlite3.connect("/Users/Prudhvi/dbstore/sqlitedb/py.db")
curs = db.cursor()
#curs.execute('create table emp2 as select * from emp1')
curs.execute('select empid, name, title from emp2')
res=curs.fetchall()
for row in res:
    print("ID: ", row[0], "Name: ", row[1], "Title: ", row[2])
db.close()

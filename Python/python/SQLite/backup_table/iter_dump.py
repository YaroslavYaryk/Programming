import sqlite3 as sq

dbd  = sq.connect("inner.db")
cur = dbd.cursor()
    
for sql in dbd.iterdump():
    print(sql)
    
dbd.commit()
dbd.close()    
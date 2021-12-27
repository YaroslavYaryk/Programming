import sqlite3 as sq


db = None
try:
    db =  sq.connect("funk.db")
    db.row_factory = sq.Row #let us print table not like 
    # a list of tuples but dictionary, extremely useful
    cur = db.cursor()
        
    # cur.execute("DROP TABLE IF EXISTS form") # delete table if it exists
    a = [("Yaroslav", 18),
        ("Olha", 16),
        ("Lidia", 48),
        ("Yuriy", 54)]
        
    cur.executescript("""CREATE TABLE IF NOT EXISTS student(
        name TEXT NOT NULL,
        age INTEGER NOT NULL
        );
        BEGIN;
        """)
    db.commit()
    
    cur.execute("SELECT * FROM student")
    
    for i in cur:
        print(i["name"], i["age"], sep = " ")

#if there is a mistake in executescriot we will get to Begin 
    
except sq.Error as er:
    if db:db.rollback()
    print("error") 
finally:
    if db:db.close()       

import sqlite3 as sq
from pprint import pprint

print = pprint

with sq.connect("Update_create.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS form") # delete table if it exists
    
    cur.execute("""CREATE TABLE IF NOT EXISTS form(
        name TEXT NOT NULL,
        age INTEGER NOT NULL DEFAULT 0,
        experiance INTEGER NOT NULL,
        score INTEGER NOT NULL DEFAULT 0
        )""")
    # cur.execute("""INSERT INTO form VALUES("YAryk", 18, 5, 1000 ) """)
    # cur.execute("""INSERT INTO form VALUES("Vova", 17, 2, 2000 )""")
    # cur.execute("""INSERT INTO form VALUES("Roma", 18, 3, 3000 )""")
    # cur.execute("""INSERT INTO form VALUES("Vasia", 17, 4, 4000 )""")
    # cur.execute("""INSERT INTO form VALUES("VAnessa", 20, 8, 9000 )""")
    # cur.execute("""INSERT INTO form VALUES("Victoria", 23, 10, 11200 )""")
    # cur.execute("""INSERT INTO form VALUES("Leila", 28, 15, 25000 )""")
    
    # cur.execute("""UPDATE form SET score = 0""")
    cur.execute("""UPDATE form SET score = 300 WHERE experiance > 5""")
    cur.execute("""DELETE FROM form WHERE experiance > 5""")
    
    
    
    
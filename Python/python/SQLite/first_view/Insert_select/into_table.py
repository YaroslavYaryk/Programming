import sqlite3 as sq
from pprint import pprint

print = pprint

with sq.connect("into_table.db") as con:
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
    
    cur.execute("""SELECT * FROM form WHERE experiance > 2 OR score > 2000 ORDER by age AND experiance """)
    # result = cur.fetchall()  #get all data from database
    # for i in result:
    #     # for j in i:
    #     #     if j == 17:
    #     #         print(17)
    #     #     elif j == 18:
    #     #         print(18)
    #     if 17 in i:
    #         print(17)
    # print(result)
    res = cur.fetchone() #return firs row of table
    res2 = cur.fetchmany(2) #return couple rows of table
    print(res)
    print(res2)
    
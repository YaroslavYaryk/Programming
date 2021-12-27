import sqlite3 as sq

db =  sq.connect("inner.db")
cur = db.cursor()
    
# cur.execute("DROP TABLE IF EXISTS form") # delete table if it exists
    
cur.execute("""CREATE TABLE IF NOT EXISTS student(
    user_id INTEGER NOT NULL,
    name TEXT Ncd..OT NULL,
    type INTEGER NOT NULL,
    experience INTEGER NOT NULL
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS marks(
    user_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    mark INTEGER NOT NULL
    )""")


cur.execute("""CREATE TABLE IF NOT EXISTS family(
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    experience INTEGER NOT NULL,
    score INTEGER NOT NULL
    )""")


db.close()
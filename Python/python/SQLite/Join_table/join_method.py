import sqlite3 as sq

db =  sq.connect("join_table.db")
cur = db.cursor()
    
# cur.execute("DROP TABLE IF EXISTS form") # delete table if it exists
    
cur.execute("""CREATE TABLE IF NOT EXISTS joins(
    user_id INTEGER NOT NULL,
    experience INTEGER NOT NULL,
    score INTEGER NOT NULL
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS names(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    score INTEGER NOT NULL
    )""")


db.close()
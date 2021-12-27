import sqlite3 as sq

with sq.connect("pract_table.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS form(
        name TEXT NOT NULL,
        age INTEGER NOT NULL DEFAULT 0,
        experiance INTEGER NOT NULL,
        score INTEGER NOT NULL DEFAULT 0
        )""")
    
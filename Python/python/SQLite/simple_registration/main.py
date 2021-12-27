import sqlite3 as sq

llogin = input("Login: ")
ppassword = input("pasword: ")


db =  sq.connect("pract_table.db")
cur = db.cursor()
    
# cur.execute("DROP TABLE IF EXISTS form") # delete table if it exists
    
cur.execute("""CREATE TABLE IF NOT EXISTS form(
    login TEXT NOT NULL,
    password INTEGER NOT NULL
    )""")

result = cur.fetchall()
for i in result:
    if llogin in i:
        print(f"Login {llogin} already exists")
        break
else:
    cur.execute("INSERT INTO form VALUES(?,?)", (llogin, ppassword) )
    db.commit()
db.close()
import sqlite3 as sq
from pprint import pprint
print = pprint

def add_to_table(user_id, score, time):
    
    cur.execute("INSERT INTO score VALUES(?,?,?)", (user_id, score, time))
    db.commit()
    


db =  sq.connect("score.db")
cur = db.cursor()

"""cur.execute() help us to make some operation  """

cur.execute("DROP TABLE IF EXISTS score") # delete table if it exists

##create table if it not exists: name = users , and other fieds below
##user_id = it's like a counter that increments when we create new row 
cur.execute("""CREATE TABLE IF NOT EXISTS score( 
    user_id INTEGER,
    score INTEGER NOT NULL DEFAULT 0,
    time INTEGER NOT NULL DEFAULT 0 
)""")

add_to_table(1,300,120)
add_to_table(2,250,300)
add_to_table(1,500,90)
add_to_table(1,900,200)
add_to_table(2,1100,270)
add_to_table(3,125,90)
add_to_table(3,700,120)
add_to_table(4,250,20)

# (cur.execute("SELECT sum(score) as score FROM score WHERE user_id = 1"))
# (cur.execute("""SELECT user_id, sum(score) as score FROM score 
#              GROUP by user_id"""))

# (cur.execute("SELECT user_id , min(time) as min, max(time) as max  FROM score GROUP BY user_id "))

(cur.execute("SELECT sum(score) as score, count() as count  FROM score GROUP BY user_id ORDER BY score DESC"))

print(cur.fetchall())

db.close()


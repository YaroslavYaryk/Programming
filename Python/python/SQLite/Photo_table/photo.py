import sqlite3 as sq


db = None
# try:
db =  sq.connect("funk.db")
db.row_factory = sq.Row #let us print table not like 
# a list of tuples but dictionary, extremely useful
cur = db.cursor()
    
try:
    def write_png(name, data): #write png file to our computer
        try:
            with open(name, "wb") as f:
                return f.write(data)
        except IOError as er:
            print(er)
            return False    
        return True
    
    
    def read_png(n): #read png file from our cimputer
        try:
            with open(f"{n}.png", "rb") as f:
                return f.read()
        except IOError as er:
            print(er)
            return False    

    cur.execute("""CREATE TABLE IF NOT EXISTS Tables(
        name TEXT,
        ava BLOB,
        score INTEGER)""")

    db.commit()


    names = [" ", "Yaroslav", "Volodia","Lidia", "Victor", "Roma"]
    prices = [0,100,200,30, 400, 500]
    for i in range(1,6):
        img = read_png(i)
        if img:
            binary = sq.Binary(img) #convert our png to special binary object
            cur.execute("INSERT INTO Tables VALUES(?,?,?)", (names[i],binary,prices[i])) #add row to the table
    db.commit()
    
    # cur.execute("SELECT ava FROM TABLES") #select all ava
    # img = cur.fetchone()["ava"] #get only one
    # write_png("new.png", img) #create new file ("new.png") 

    
    
except sq.Error as er:
    if db:db.rollback()
    print(er) 
finally:
    if db:db.close()       

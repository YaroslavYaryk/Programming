import sqlite3 as sq


with sq.connect("saper_table.db") as con:  # open the sql object

    cur = con.cursor()  # create the main object

    """cur.execute() help us to make some operation  """
    cur.execute("DROP TABLE IF EXISTS users")  # delete table if it exists
    # create table if it not exists: name = users , and other fieds below
    # user_id = it's like a counter that increments when we create new row
    cur.execute(
            """CREATE TABLE IF NOT EXISTS users( 
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        old INTEGER NOT NULL DEFAULT 0,
        score INTEGER NOT NULL DEFAULT 0 
    )"""
    )

# we don't have to close the sql project because we use context-manager

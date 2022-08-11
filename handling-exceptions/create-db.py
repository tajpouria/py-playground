import sqlite3

conn = sqlite3.connect("application.db")

cur = conn.cursor()

cur.execute(
    """CREATE TABLE blogs
                (id text not null primary key, data text, title text, content text, public integer)
"""
)

cur.execute(
    "INSERT INTO blogs VALUES ('first-blog', '2022-03-07', 'My first blog', 'Some Content', 1)"
)
cur.execute(
    "INSERT INTO blogs VALUES ('private-blog', '2022-03-07', 'My private blog', 'This is a secret', 0)"
)

conn.commit()

conn.close()

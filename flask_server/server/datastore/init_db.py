import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (email,password,fullname,role,address,gender,license) VALUES (?,?,?,?,?,?,?)",
            ('test@gmail.com', 'test', 'Nathan A-K', 'admin','school','male',1))
connection.commit()
connection.close()
import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (email,password,fullName,role,address,gender,license) VALUES (?,?,?,?,?,?,?)",
            ('test@gmail.com', 'test', 'Nathan A-K', 'admin','school','male',1))
connection.commit()
connection.close()
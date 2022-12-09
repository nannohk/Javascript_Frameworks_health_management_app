import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (email,password,fullName,role,address,gender,license) VALUES (?,?,?,?,?,?,?)",
            ('admin@gmail.com', 'test', 'Nathan A-K', 'admin','school','male',True))
cur.execute("INSERT INTO user (email,password,fullName,role,address,gender,license) VALUES (?,?,?,?,?,?,?)",
            ('manager@gmail.com', 'test', 'Jane Doe', 'manager','school','female',True))
connection.commit()
connection.close()
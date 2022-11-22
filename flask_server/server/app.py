import sqlite3
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('/datastore/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=('POST'))
def index():
    title = request.form['title']
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',(title, content))
    conn.commit()
    conn.close()
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
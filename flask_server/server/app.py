import sqlite3
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# Database section
# ****************************************************************************
def get_db_connection():
    conn = sqlite3.connect('./datastore/database.db')
    conn.row_factory = sqlite3.Row
    return conn

sqlInt = 'INSERT INTO users (email, password,role) VALUES(?,?,?)'
sqlUpdate = 'UPDATE users SET fullname = ?,address=?, gender=?, license=? WHERE email = ?'
sqlSelect = 'SELECT email, password,role,fullname FROM users WHERE email = ? and password = ?'

def updateData(email, fullname, address, gender, license):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sqlUpdate, (fullname, address, gender, license, email))
    conn.commit()
    conn.close()
    if cur != None:
        return {'message': 'profile updated'}
    else:
        return {'message': 'profile not updated'}

def insertData(email, password, role):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sqlInt, (email, password, role))
    conn.commit()
    conn.close()
    if cur != None:
        return {'message': 'user created'}
    else:
        return {'message': 'user not created'}

def loginData(email, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sqlSelect, (email, password))
    rows = cur.fetchall()
    role = ''
    fullname = ''
    for row in rows:
        role = row[2]
        fullname = row[3]

    conn.close()
    if rows != None:
        return { 'status':'success','role':role,'fullname':fullname, 'auth':True}
    else:
        return {'message': 'Login failed', 'auth':False}

def selectAdminList():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('email,fullname,role,profileImage,address,gender,license from users')
    rows = cur.fetchall()
    conn.close()
    if rows != None:
        return { 'message':rows}
    else:
        return {'message': 'Failed to obtain all users'}

def selectClientData(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select email,password,fullname,role,profileImage,address,gender,license from users where email = ?')
    rows = cur.fetchall()
    conn.close()
    if rows != None:
        return { 'list':rows,'message':'Display success'}
    else:
        return {'message': 'Failed to obtain user data'}

# End of Database section
# ****************************************************************************



# @app.route('/', methods=["POST"])
# def index():
#     title = data['title']
#     conn = get_db_connection()
#     conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',(title, content))
#     conn.commit()
#     conn.close()
#     return "Hello World!"

@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    return loginData(email, password)

@app.route('/signUp', methods=["POST"])
def signUp():
    data = request.get_json()
    email = data['email']
    password = data['password']
    role = data['role']
    return insertData(email, password, role)

@app.route('/updateProfile', methods=["POST"])
def updateProfile():
    data = request.get_json()
    email = data['email']
    fullname = data['fullName']
    address = data['address']
    gender = data['gender']
    license = data['license']
    return updateData(email, fullname, address, gender, license)

@app.route('/getAdminList', methods=["POST"])
def getAdminList():
    return selectAdminList()

@app.route('/getClientData', methods=["POST"])
def getClientData():
    data = request.get_json()
    email = data['email']
    return selectClientData(email)



if __name__ == '__main__':
    app.run(debug=True)
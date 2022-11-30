import sqlite3
import json
import base64
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
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


sqlInt = 'INSERT INTO user (email, password,role) VALUES(?,?,?)'
sqlUpdate = 'UPDATE user SET fullName = ?,address=?, gender=?, license=?,phoneNumber=? WHERE email = ?'
sqlLoginSelect = 'SELECT email, password,role,fullname FROM user WHERE email = ? and password = ?'


def updateData(email, fullname, address, gender, license):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sqlUpdate, (fullname, address, gender, license, email))
    conn.commit()
    conn.close()
    if cur != None:
        return {'message': 'profile updated', 'status': 'success'}
    else:
        return {'message': 'profile not updated', 'status': 'failed'}


def saveProfile(file, email):
    # Convert Image files to binary
    convertedFile = file.read()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE user SET profileImage=? WHERE email = ?',
                (convertedFile, email))
    conn.commit()
    conn.close()


def signUpData(email, password, role):
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
    cur.execute(sqlLoginSelect, (email, password))
    rows = cur.fetchall()
    role = ''
    fullname = ''
    for row in rows:
        role = row[2]
        fullname = row[3]

    conn.close()
    if rows != None:
        return {'status': 'success', 'role': role, 'fullname': fullname, 'auth': True}
    else:
        return {'message': 'Login failed', 'auth': False}


def selectAdminList():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'select email,fullname,role,profileImage,address,gender,license from user')
    rows = cur.fetchall()
    rows = [dict(ix) for ix in rows]
    newrows = []
    for row in rows:
        img = row['profileImage']
        if img != None:
            img = base64.b64encode(img).decode('utf-8')
        newrows.append({'email': row['email'], 'fullname': row['fullname'], 'role': row['role'], 'profileImage': img, 'address': row,
                    'profileImage': img, 'address': row['address'], 'gender': row['gender'], 'license': row['license']})

    conn.close()
    if rows != None:
        return {'list':newrows,'status': 'success'}
    else:
        return {'message': 'Failed to obtain all users'}


def selectClientData(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'select email,password,fullname,role,profileImage,address,gender,license from user where email = ?', [email])
    rows = cur.fetchall()
    img = rows[0]['profileImage']
    img = base64.b64encode(img).decode('utf-8')
    newrow = {'email': rows[0]['email'], 'password': rows[0]['password'], 'fullname': rows[0]['fullname'], 'role': rows[0]
              ['role'], 'profileImage': img, 'address': rows[0]['address'], 'gender': rows[0]['gender'], 'license': rows[0]['license']}
    conn.close()
    if rows != None:
        return {'list': newrow, 'status': 'success'}
    else:
        return {'message': 'Failed to obtain user data'}

# End of Database section
# ****************************************************************************


# API section
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
    return signUpData(email, password, role)


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


@app.route('/profileUpload', methods=["POST"])
def profileUpload():
    if 'file' not in request.files:
        return {'message': 'No file part'}
    else:
        file = request.files['file']
        email = request.form['newFileName']
        saveProfile(file, email)
        # file.save('./datastore/'+email+'.png')
        return {'status': 'success'}


if __name__ == '__main__':
    app.run(debug=True)
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


def signUpPatient(fullName, gender, address, patientImage, phoneNumber, employer, employerAddress, position, dateOfBirth,
                  caregiverEmail, caregiverName, econtactName, econtactRelation, econtactAddress, econtactPhoneNumber,
                  insuranceCompany, insuredParty, policyNumber, groupNumber, relationship):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO patient (fullName,gender,address,patientImage,phoneNumber,employer,employerAddress,position,dateOfBirth,caregiverEmail,caregiverName,econtactName,econtactRelation,econtactAddress,econtactPhoneNumber) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
    (fullName, gender, address, patientImage, phoneNumber, employer, employerAddress, position, dateOfBirth,caregiverEmail, caregiverName, econtactName, econtactRelation, econtactAddress, econtactPhoneNumber))
    conn.commit()
    patientId = cur.execute('select id from patient where fullName=? AND address=? AND phoneNumber=?', (fullName, address, phoneNumber))
    patientId =patientId.fetchall()
    patientId = patientId[0][0]
    cur.execute('INSERT INTO insurance (patientId,insuranceCompany,insuredParty,policyNumber,groupNumber,relationship) VALUES(?,?,?,?,?,?)',(patientId,insuranceCompany, insuredParty, policyNumber, groupNumber, relationship))
    conn.commit()
    conn.close()

    if cur != None:
        return {'status': 'success'}
    else:
        return {'status': 'Patient not created'}


def updateData(email, fullname, address, gender, license, phoneNumber):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sqlUpdate, (fullname, address,
                gender, license, phoneNumber, email))
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
    if cur != None:
        return {'message': 'profile image updated', 'status': 'success'}
    else:   
        return {'message': 'profile image not updated', 'status': 'failed'}


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
        'select email,fullName,role,profileImage,address,gender,phoneNumber,license from user')
    rows = cur.fetchall()
    rows = [dict(ix) for ix in rows]
    newrows = []
    for row in rows:
        img = row['profileImage']
        if img != None:
            img = base64.b64encode(img).decode('utf-8')
        newrows.append({'email': row['email'], 'fullname': row['fullName'], 'role': row['role'],
                        'profileImage': img, 'address': row['address'], 'gender': row['gender'], 'license': row['license'], 'phoneNumber': row['phoneNumber']})

    conn.close()
    if rows != None:
        return {'list': newrows, 'status': 'success'}
    else:
        return {'message': 'Failed to obtain all users'}


def selectCaregiverList():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'select email,fullName,role,profileImage,address,gender,phoneNumber,license from user where role = "caregiver"')
    rows = cur.fetchall()
    rows = [dict(ix) for ix in rows]
    newrows = []
    for row in rows:
        img = row['profileImage']
    # if img != None | type(img) == bytes:
        #     img = base64.b64encode(img).decode('utf-8')
        newrows.append({'email': row['email'], 'fullname': row['fullName'], 'role': row['role'],
                        'profileImage': img, 'address': row['address'], 'gender': row['gender'], 'license': row['license'], 'phoneNumber': row['phoneNumber']})

    conn.close()
    if rows != None:
        return {'list': newrows, 'status': 'success'}
    else:
        return {'message': 'Failed to obtain all users'}


def selectPatientList():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from patient')
    # cur.execute('select gender,fullName,address,patientImage,phoneNumber,employer,employerAddress,position,dateOfBirth,caregiverEmail,caregiverName from patient')
    rows = cur.fetchall()
    rows = [dict(ix) for ix in rows]
    newrows = []
    for row in rows:
        img = row['patientImage']
    # if img != None:
        #     img = base64.b64encode(img).decode('utf-8')
        newrows.append({'fullname': row['fullName'], 'patientImage': img, 'address': row['address'], 'gender': row['gender'],
                        'phoneNumber': row['phoneNumber'], 'caregiverEmail': row['caregiverEmail'], 'caregiverName': row['caregiverName']})
    conn.close()
    if rows != None:
        return {'list': newrows, 'status': 'success'}
    else:
        return {'message': 'Failed to obtain all patients'}

def selectMyPatients(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select fullName,patientImage,address,gender,phoneNumber from patient where caregiverEmail = ?',[email])
    # cur.execute('select gender,fullName,address,patientImage,phoneNumber,employer,employerAddress,position,dateOfBirth,caregiverEmail,caregiverName from patient')
    rows = cur.fetchall()
    rows = [dict(ix) for ix in rows]
    newrows = []
    for row in rows:
        img = row['patientImage']
        # if img != None:
        #     img = base64.b64encode(img).decode('utf-8')
        newrows.append({'fullname': row['fullName'], 'patientImage': img, 'address': row['address'], 'gender': row['gender'],
                        'phoneNumber': row['phoneNumber']})
    conn.close()
    if rows != None:
        return {'list': newrows, 'status': 'success'}
    else:
        return {'message': 'Failed to obtain all patients'}

def selectClientData(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'select email,fullname,role,profileImage,address,gender,license,phoneNumber from user where email = ?', [email])
    rows = cur.fetchall()
    img = rows[0]['profileImage']
    if img != None:
        img = base64.b64encode(img).decode('utf-8')
    newrow = {'email': rows[0]['email'], 'fullname': rows[0]['fullname'], 'role': rows[0]
              ['role'], 'phoneNumber': rows[0]['phoneNumber'], 'profileImage': img, 'address': rows[0]['address'], 'gender': rows[0]['gender'], 'license': rows[0]['license']}
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
    phoneNumber = data['phoneNumber']
    return updateData(email, fullname, address, gender, license, phoneNumber)


@app.route('/getAdminList', methods=["POST"])
def getAdminList():
    return selectAdminList()


@app.route('/getCaregiverList', methods=["POST"])
def getCaregiverList():
    return selectCaregiverList()


@app.route('/getPatientList', methods=["POST"])
def getPatientList():
    return selectPatientList()


@app.route('/getClientData', methods=["POST"])
def getClientData():
    data = request.get_json()
    email = data['email']
    return selectClientData(email)

@app.route('/getMyPatients', methods=["POST"])
def getMyPatients():
    data = request.get_json()
    email = data['email']
    return selectMyPatients(email)

@app.route('/profileUpload', methods=["POST"])
def profileUpload():
    if 'file' not in request.files:
        return {'message': 'No file part'}
    else:
        file = request.files['file']
        email = request.form['newFileName']
        return saveProfile(file, email)
        # file.save('./datastore/'+email+'.png')


@app.route('/addPatient', methods=["POST"])
def addPatient():
    data = request.get_json()
    fullName = data['fullName']
    gender = data['gender']
    address = data['address']
    patientImage = data['patientImage']
    phoneNumber = data['phoneNumber']
    employer = data['employer']
    employerAddress = data['employerAddress']
    position = data['position']
    dateOfBirth = data['dateOfBirth']
    caregiverEmail = data['caregiverEmail']
    caregiverName = data['caregiverName']
    econtactName = data['econtactName']
    econtactRelation = data['econtactRelation']
    econtactAddress = data['econtactAddress']
    econtactPhoneNumber = data['econtactPhoneNumber']
    insuranceCompany = data['insuranceCompany']
    insuredParty = data['insuredParty']
    policyNumber = data['policyNumber']
    groupNumber = data['groupNumber']
    relationship = data['relationship']
    return signUpPatient(fullName, gender, address, patientImage, phoneNumber, employer, employerAddress, position, dateOfBirth,
                         caregiverEmail, caregiverName, econtactName, econtactRelation, econtactAddress, econtactPhoneNumber,
                         insuranceCompany, insuredParty, policyNumber, groupNumber, relationship)


if __name__ == '__main__':
    app.run(debug=True)

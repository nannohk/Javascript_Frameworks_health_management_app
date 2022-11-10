const express = require('express');
const app = express();
const cors = require('cors');
const e = require('express');
app.use(cors());
app.set('port', '1500');
app.use(express.json({ limit: '1mb' }));
app.listen(1500, () => console.log('Server running on port 1500'));

/***************************************************************************************************** */
//Database information
//db.run('drop table if exists users');

// db.run('CREATE TABLE users (email Varchar2(100) PRIMARY KEY, password Varchar2(100),fullname varchar2(200),role varchar2(100),
//profileImage blob,address varchar2(200),gender varchar2(10),license boolean)');
// db.run('CREATE view admin_list as select email,fullname,role,gender,address,license from users');

// db.close((err) => {
//     if (err) return console.error(err.message);
// });

let authStatus = false;
const sqlInt = `INSERT INTO users (email, password,role) VALUES(?,?,?)`;
const sqlUpdate = `UPDATE users SET fullname = ?,address=?, gender=?, license=? WHERE email = ?`;
const sqlSelect = `SELECT email, password FROM users WHERE email = ? and password = ?`;
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./datastore/serverDB.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) return console.error(err.message);
    console.log('Connected to the project database.');
});


function updateData(email, fullname, address, gender, license) {
    return new Promise((resolve, reject) => {
        db.run(sqlUpdate, [fullname, address, gender, license, email], function (err) {
            if (err) {
                reject(err);
            } else {
                resolve({
                    message: 'profile updated'
                });
            }
        });
    });
}

function insertData(email, password,role) {
    db.run(sqlInt, [email, password,role],
        function (err) {
            if (err) return console.error(err.message);
            console.log(`A row has been inserted with rowid ${this.lastID}`);
        });
}

function selectData(email, password) {
    return new Promise((resolve, reject) => {
        db.all(sqlSelect, [email, password], (err, rows) => {
            if (err || rows.length == 0) {
                reject({
                    message: err,
                    auth: false
                });
            }
            else {
                resolve({
                    message: rows,
                    auth: true
                });
            }
        });
    });
}

function selectAdminList() {
    return new Promise((resolve, reject) => {
        db.all('select * from admin_list', (err, rows) => {
            if (err) {
                reject(err);
            }
            else {
                resolve(rows);
            }
        });
    });
}
/******************************************************************************************************* */



app.post('/', (request, response) => {
    //insert data passed from client to database
    if (request.body.purpose == "signup") {
        insertData(request.body.email, request.body.password,request.body.role);
        response.json({
            status: 'creation success',
        });
    }
    else if (request.body.purpose == "login") {
        console.log("login request");
        //  insertData('client@gmail.com', 'client');
        selectData(request.body.email, request.body.password).then((sol) => {
            console.log("login success");
            response.json({
                status: 'success',
            });
        }).catch((err) => {
            console.log("login failed");
            response.json({
                status: 'failed',
            });
        });
    }
    else if (request.body.purpose == "profileUpdate") {
        console.log("profile update request");
        updateData(request.body.email, request.body.fullName, request.body.address, request.body.gender,
            request.body.license).then((sol) => {
                console.log("profile update success");
                response.json({
                    status: 'success',
                });
            }).catch((err) => {
                console.log("profile update failed");
                response.json({
                    status: 'failed',
                });
            });
    }
    else if (request.body.purpose == "getAdminList") {
        console.log("admin list request");
        selectAdminList().then((sol) => {
            console.log("admin list success");
            response.json({
                status: 'success',
                list: sol
            });
        }).catch((err) => {
            console.log("admin list failed");
            response.json({
                status: 'failed',
            });
        });
    }

});
const express = require('express');
const multer = require('multer');
const app = express();
const cors = require('cors');
const e = require('express');
const { response } = require('express');
app.use(cors());
app.set('port', '1500');
app.use(express.json({ limit: '1mb' }));
app.listen(1500, () => console.log('Server running on port 1500'));
const upload = multer({
    dest: './datastore/uploads/',
});

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
const sqlSelect = `SELECT email, password,role,fullname FROM users WHERE email = ? and password = ?`;
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

function insertData(email, password, role) {
    db.run(sqlInt, [email, password, role],
        function (err) {
            if (err) return console.error(err.message);
            console.log(`A row has been inserted with rowid ${this.lastID}`);
        });
}

function loginData(email, password) {
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
        db.all('select email,fullname,role,profileImage,address,gender,license from users', (err, rows) => {
            if (err) {
                reject(err);
            }
            else {
                resolve(rows);
            }
        });
    });
}

function selectClientData(email) {
    return new Promise((resolve, reject) => {
        db.all('select email,password,fullname,role,profileImage,address,gender,license from users where email = ?', [email], (err, rows) => {
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

app.post('/upload', upload.single('file'), (req, res) => {
    res.json({cool: 'cool'});
});
    
app.post('/', (request, response) => {
    console.log(request);
    //insert data passed from client to database
    if (request.body.purpose == "signup") {
        insertData(request.body.email, request.body.password, request.body.role);
        response.json({
            status: 'creation success',
        });
    }
    else if (request.body.purpose == "login") {
        console.log("login request");
        loginData(request.body.email, request.body.password).then((sol) => {
            console.log("login success");
            response.json({
                status: 'success',
                role: sol.message[0].role,
                fullname: sol.message[0].fullname,
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
    else if (request.body.purpose == "getClientData") {
        console.log("client data request");
        selectClientData(request.body.email).then((sol) => {
            console.log("client data success");
            response.json({
                status: 'success',
                list: sol
            });
        }).catch((err) => {
            console.log("client data failed");
            response.json({
                status: 'failed',
            });
        });
    }

});
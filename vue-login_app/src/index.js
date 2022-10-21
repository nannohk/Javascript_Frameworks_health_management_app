import { data } from 'Login-page.vue'

const email = data().email;
const password = data().password;
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./database/vue_pj.db',sqlite3.OPEN_READWRITE, (err) => {
    if (err) return console.error(err.message);

    console.log('Connected to the SQlite database.');
});


db.all(`SELECT email, password FROM users where email=${email} AND password=${password};`, [], (err, rows) => {
    if (err) return console.error(err.message);
    rows.forEach((row) => {
        console.log(row);
    });
});

db.close((err) => {
    if (err) return console.error(err.message);
});


// db.run('CREATE TABLE users (email Varchar2(100), password Varchar2(100))');

// const sql = `INSERT INTO users (email, password) VALUES(?,?)`;

// db.run(sql, ['john@yahoo.com','pass1234'],
//  function(err){
//     if (err) return console.error(err.message);
//     console.log(`A row has been inserted with rowid ${this.lastID}`);
// });

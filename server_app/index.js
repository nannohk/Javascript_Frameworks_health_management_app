const express = require('express');
const app = express();
app.listen(1500, () => console.log('Server running on port 1500'));
app.use(express.static('public'));
app.use(express.json({ limit: '1mb' }));

/***************************************************************************************************** */
//Database information
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./datastore/serverDB.db',sqlite3.OPEN_READWRITE, (err) => {
    if (err) return console.error(err.message);

    console.log('Connected to the project database.');
});

// db.run('CREATE TABLE users (email Varchar2(100) PRIMARY KEY, password Varchar2(100))');

const sql = `INSERT INTO users (email, password) VALUES(?,?)`;

db.run(sql, ['jane@yahoo.com','pass1234'],
 function(err){
    if (err) return console.error(err.message);
    console.log(`A row has been inserted with rowid ${this.lastID}`);
});


/******************************************************************************************************* */
app.post('/api',(request,response) =>{
    console.log("I got a request");
    response.json({
        status: 'success',
    });
});

db.close((err) => {
    if (err) return console.error(err.message);
});

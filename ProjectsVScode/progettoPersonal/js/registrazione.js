class Member {
    static id = 0;
    constructor(name, email, password) {
        this.name = name;
        this.id = Member.id++;
        this.email = email;
        this.password = password;
    }

    get_id() {
        console.log(`Your ID: ${this.id}`);
    }
}

class Database {
    constructor() {
        this.registrazione = {};
    }

    controllo(membri) {
        const dominio_email = ["gmail.com", "yahoo.com", "ymail.com", "rocketmail.com", "outlook.com", "hotmail.com", "live.com"];
        const map = ["!", "?", "*", "£", "$", "%", "=", "^", "§"];
        const num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
    
        const [nome, dominio] = membri.email.split("@");
    
        if (membri.password.length < 10) {
            console.log('La password deve avere almeno 10 caratteri');
            return false;
        }
    
        if (!map.some(car => membri.password.includes(car))) {
            console.log('Deve contenere un carattere speciale');
            return false;
        }
    
        if (!num.some(char => membri.password.includes(char))) {
            console.log('Inserisci almeno un numero');
            return false;
        }
    
        if (!dominio_email.some(dom => dominio.includes(dom))) {
            console.log('Il dominio non è conforme');
            return false;
        }
    
        if (!membri.password.some(mai => mai.toUpperCase() === mai)) {
            console.log("Deve avere almeno un carattere maiuscolo");
            return false;
        }
    
        return true;
    }

    db_registra(membri) {
        if (!this.controllo(membri)) {
            return 'Utente non registrato';
        }
    
        if (membri.id in this.registrazione) {
            return "Sei già nel DataBase";
        }
    
        this.registrazione[membri.id] = [membri.name, membri.email, membri.password];
        return `Utente registrato con ID ${membri.id}`;
    }

    tutti() {
        let lista = [];
        for (let k in this.registrazione) {
            lista.push(this.registrazione[k][0]);  // Add only the name to the list
        }
        return lista;
    }
}

const db = new Database();

// Express.js code for the web application
const express = require('express');
const app = express();
const path = require('path');

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '../html/css')));
app.set('views', path.join(__dirname, '../html'));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('pagReg', { message: '', members: db.tutti() });
});

app.post('/', (req, res) => {
    const name = req.body.name;
    const email = req.body.email;
    const password = req.body.password;
    const member = new Member(name, email, password);
    const message = db.db_registra(member);
    res.render('pagReg', { message: message, members: db.tutti() });
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});
import sqlite3

# Creare una connessione al database SQLite (crea il database se non esiste)
conn = sqlite3.connect('example.db')

# Creare un cursore per eseguire comandi SQL
cursor = conn.cursor()

# Creare una tabella
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Inserire alcuni dati nella tabella
users = [
    ('Alice', 30, 'alice@example.com'),
    ('Bob', 25, 'bob@example.com'),
    ('Charlie', 35, 'charlie@example.com')
]

cursor.executemany('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', users)

# Confermare le modifiche
conn.commit()

# Recuperare e visualizzare i dati dalla tabella
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Chiudere la connessione al database
conn.close()

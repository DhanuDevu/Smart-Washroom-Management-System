from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL
     )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL
     )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mentain (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL
     )
''')
conn.commit()
conn.close()


# Home route (renders both forms)
@app.route('/')
def index():
    return render_template('index.html')

# Home route (renders both forms)
@app.route('/mentain')
def mentain():
    return render_template('index.html')

# Home route (renders both forms)
@app.route('/admin')
def admin():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    password = request.form['password']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    conn.commit()
    conn.close()
    return render_template('index.html', msg="Registration successfull")

@app.route('/signin', methods=['POST'])
def signin():
    name = request.form['name']
    password = request.form['password']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (name, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return render_template('logged.html')
    else:
        return render_template('index.html', msg="Entered wrong credantials")


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

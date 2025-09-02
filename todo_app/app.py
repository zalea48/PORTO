from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3, os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key-change-me'
DB = 'tasks.db'

def init_db():
    if not os.path.exists(DB):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            due_time TEXT,
            category TEXT,
            created_at TEXT,
            completed INTEGER DEFAULT 0
        )''')
        conn.commit()
        conn.close()

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    rows = query_db('SELECT * FROM tasks ORDER BY completed, due_date IS NULL, due_date, due_time')
    tasks = [dict(r) for r in rows]
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date') or None
    due_time = request.form.get('due_time') or None
    category = request.form.get('category') or 'Fleksibel'
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M')
    query_db('INSERT INTO tasks (title,description,due_date,due_time,category,created_at) VALUES (?,?,?,?,?,?)',
             (title, description, due_date, due_time, category, created_at))
    flash('Task added')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_task(id):
    if request.method == 'GET':
        r = query_db('SELECT * FROM tasks WHERE id=?', (id,), one=True)
        return render_template('edit.html', task=dict(r))
    else:
        title = request.form.get('title')
        description = request.form.get('description')
        due_date = request.form.get('due_date') or None
        due_time = request.form.get('due_time') or None
        category = request.form.get('category') or 'Fleksibel'
        query_db('UPDATE tasks SET title=?,description=?,due_date=?,due_time=?,category=? WHERE id=?',
                 (title,description,due_date,due_time,category,id))
        flash('Task updated')
        return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    query_db('DELETE FROM tasks WHERE id=?', (id,))
    flash('Task deleted')
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle_complete(id):
    r = query_db('SELECT completed FROM tasks WHERE id=?', (id,), one=True)
    if r:
        new = 0 if r['completed'] else 1
        query_db('UPDATE tasks SET completed=? WHERE id=?', (new, id))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

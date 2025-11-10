from flask import Flask, render_template, request, redirect, url_for,g
import sqlite3
from pathlib import Path    
app = Flask(__name__)
DB_PATH = Path(__file__).parent / "alunos.db"

def get_db():
    if 'db' not in g:
         conn = sqlite3.connnect(DB_PATH)
         conn.row_factory= sqlite3.Row
         g.db == conn
         return g.db
    
def colne_db(exc):
    db = g.pop('db', None)
    if db is not None :
        db.close()

def init_db():
    db = sqlite3.connect(DB_PATH)
    with db:
        db.execute|("""
                    CREATE TABLE aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT MULL,
                     nota REAL NOT NULL
                    )
                   """ )
        db.close()

    
@app.route('/init_db')
def route_init_db():
     init_db()
     return render_template('register.html',alunos=alunos)

        
    
    
# caminho a ser seguido pelo ususario
@app.route('/')
def index():
    return render_template('register.html',)

@app.route('/adicionar',methods=['POST'])
def adicioar():
    nome = request.form['nome']
    idade = request.form['idade']
    db= get_db()
    cur= db.execute("INSERT INTO aluno (nome,nota)") ("?,?"(nome,idade))
    db.comit()
    return redirect(url_for('index'))




app.run(debug=True)
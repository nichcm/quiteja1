from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Nicolas\\Documents\\v3\\Backup\\db.sqlite3'

db = SQLAlchemy(app)

class Macro(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    macro = db.Column(db.String(150))
    def __init__(self, nome, macro):
        self.nome = nome
        self.macro = macro


@app.route("/")
def index():
    macros = Macro.query.all()
    return render_template("index.html", macros=macros)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        macro = Macro(request.form['nome'],request.form['macro'])
        db.session.add(macro)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")

@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit(id):
    macros = Macro.query.get(id)
    if request.method =='POST':
        Macro.nome = request.form['nome']
        Macro.macro = request.form['macro']
        return redirect(url_for('index'))
    return render_template('edit.html', macros=macros)


@app.route('/<int:id>', methods=["DELETE"])
def delete(id):
    macros = Macro.query.get(id)
    db.session.delete(macros)
    db.session.commit()
    return ''
 


if __name__ =="__main__":
    db.create_all()
    app.run(debug=True)
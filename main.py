from flask import *
import sqlite3
from functools import wraps
app = Flask(__name__)
SECRET_KEY = 'tp_bd'
USERNAME = 'Guidio'
PASSWORD = '123'
app.config.from_object(__name__)

is_logged = False
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
        if user == USERNAME:
            if passw == PASSWORD:
                return indexLogged(True)

    return render_template('login.html')

@app.route('/Logged', methods=['GET'])
def indexLogged(is_logged):
    with sqlite3.connect('sql/skills.db') as con:
        cur = con.cursor()
        x = cur.execute("SELECT * from SKILLS WHERE nota >= 9")
        rows = x.fetchall()
        skills = [dict(nome_skill=row[0], nota=row[1] * 10) for row in rows]
        y = cur.execute("SELECT * from SKILLS WHERE nota < 9")
        rows_resto = y.fetchall()
        skills_resto = [dict(nome_skill=row[0], nota=row[1] * 10) for row in rows_resto]
        con.commit()

        cur = con.cursor()
        x = cur.execute("SELECT * from ESTUDOS")
        rows = x.fetchall()
        estudos = [dict(lugar=row[0], ano=row[1], tipo=row[2]) for row in rows]
        con.commit()

        cur = con.cursor()
        x = cur.execute("SELECT * from LANGUAGES")
        rows = x.fetchall()
        langs = [dict(nome_lingua=row[0], nota=row[1] * 10) for row in rows]
        con.commit()
    sqlite3.connect('sql/skills.db').close()
    return render_template('index.html', rec=skills, rec_resto=skills_resto, rec2=estudos, rec3=langs, logged=is_logged)

@app.route('/', methods=['GET'])
def index():
    with sqlite3.connect('sql/skills.db') as con:
        cur = con.cursor()
        x = cur.execute("SELECT * from SKILLS WHERE nota >= 9")
        rows = x.fetchall()
        skills = [dict(nome_skill=row[0], nota=row[1] * 10) for row in rows]
        y = cur.execute("SELECT * from SKILLS WHERE nota < 9")
        rows_resto = y.fetchall()
        skills_resto = [dict(nome_skill=row[0], nota=row[1] * 10) for row in rows_resto]
        con.commit()

        cur = con.cursor()
        x = cur.execute("SELECT * from ESTUDOS")
        rows = x.fetchall()
        estudos = [dict(lugar=row[0], ano=row[1], tipo=row[2]) for row in rows]
        con.commit()

        cur = con.cursor()
        x = cur.execute("SELECT * from LANGUAGES")
        rows = x.fetchall()
        langs = [dict(nome_lingua=row[0], nota=row[1] * 10) for row in rows]
        con.commit()
    sqlite3.connect('sql/skills.db').close()
    return render_template('index.html', rec=skills, rec_resto=skills_resto, rec2=estudos, rec3=langs, logged=is_logged)

@app.route('/fill_skills')
def nameWIP():
    return render_template('add_skills.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/mysql', methods=['POST', 'GET'])
def nameWIP2():
    with sqlite3.connect('sql/skills.db') as con:
        if (request.method == 'POST'):
            cur = con.cursor()
            insert = []
            for i in request.form:
                insert.append(request.form[i])
            x = cur.execute(
                "SELECT * FROM SKILLS WHERE nome_skill = ? OR nota = ?", [insert[0], insert[1]]
            )
            rows = x.fetchall()
            skills = [dict(nome_skill=row[0], nota=row[1]) for row in rows]
            x = cur.execute(
                "SELECT * FROM ESTUDOS WHERE lugar = ?", [insert[2]]
            )
            rows = x.fetchall()
            estudos = [dict(lugar=row[0], ano=row[1], tipo=row[2]) for row in rows]
            x = cur.execute(
                "SELECT * FROM LANGUAGES WHERE nome_lingua = ? OR nota = ?", [insert[3], insert[1]]
            )
            rows = x.fetchall()
            linguas = [dict(nome_lingua=row[0], nota=row[1]) for row in rows]
            con.commit()
            return render_template('MySQL.html', rec=skills, rec2=estudos, rec3=linguas)
        else:
            cur = con.cursor()
            x = cur.execute("SELECT * from SKILLS ")
            rows = x.fetchall()
            skills = [dict(nome_skill=row[0], nota=row[1]) for row in rows]
            con.commit()

            cur = con.cursor()
            x = cur.execute("SELECT * from ESTUDOS")
            rows = x.fetchall()
            estudos = [dict(lugar=row[0], ano=row[1], tipo=row[2]) for row in rows]
            con.commit()

            cur = con.cursor()
            x = cur.execute("SELECT * from LANGUAGES")
            rows = x.fetchall()
            langs = [dict(nome_lingua=row[0], nota=row[1]) for row in rows]
            con.commit()
            return render_template('MySQL.html', rec=skills, rec2=estudos, rec3=langs)
    sqlite3.connect('sql/skills.db').close()
    return render_template('MySQL.html')


@app.route('/look_up_tables', methods=['GET', 'POST'])
def nameWIP4():
    print(request.form)
    with sqlite3.connect('sql/skills.db') as con:
        cur = con.cursor()
        print(request.form['val1'])
        x = cur.execute("SELECT * FROM SKILLS WHERE nome_skill = ?", [request.form['val1']])
        rows = x.fetchall()
        skills = [dict(nome_skill=row[0], nota=row[1]) for row in rows]
        con.commit()
    return render_template('MySQL.html', rec=skills)


@app.route('/add_skills', methods=['GET', 'POST'])
def nameWIP3():
    if (request.method == 'POST'):
        if request.method == 'POST':
            with sqlite3.connect('sql/skills.db') as con:
                insert = [
                    request.form['nome_skill'],
                    request.form['nota'],
                ]
                if None in insert:
                    flash("Por favor preencha todos os campos")
                    return redirect('/')
                else:
                    cur = con.cursor()
                    if insert[0] != '':
                        cur.execute(
                            "REPLACE INTO SKILLS (nome_skill, nota) values (?, ?)",
                            [insert[0], insert[1]])
                        con.commit()
                        return redirect('/')
                    else:
                        return redirect('/')
    return render_template('index.html')


@app.route('/remove_skills')
def nameWIP6():
    return render_template('remove_skills.html')


@app.route('/tira_skills', methods=['GET', 'POST'])
def nameWIP5():
    if (request.method == 'POST'):
        if request.method == 'POST':
            with sqlite3.connect('sql/skills.db') as con:
                insert = [
                    request.form['nome_skill']
                ]
                if None in insert:
                    flash("Por favor preencha todos os campos")
                    return redirect('/')
                else:
                    cur = con.cursor()
                    cur.execute(
                        "DELETE FROM SKILLS WHERE nome_skill = ?",
                        [insert[0]])
                    con.commit()
                    return redirect('/')
    return render_template('index.html')

def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

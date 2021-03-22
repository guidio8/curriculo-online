from flask import *
import sqlite3

app = Flask(__name__)
SECRET_KEY = 'tp_bd'
USERNAME = 'Guidio'
PASSWORD = '123'
app.config.from_object(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
        if user == USERNAME:
            if passw == PASSWORD:
                return index(True)

    return render_template('login.html')

@app.route('/en', methods=['GET'])
def translateEnglish():
    return index('en')

@app.route('/pt', methods=['GET'])
def translatePortugues():
    return index('pt')

@app.route('/', methods=['GET'])
def index(*args):
    language = 'pt'

    if True in args:
        is_logged = True
    else:
        is_logged = False

    if 'en' in args:
        language = 'en'

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
    return render_template('index.html', rec=skills, rec_resto=skills_resto, rec2=estudos, rec3=langs, logged=is_logged, language=language)

@app.route('/fill_skills')
def nameWIP():
    return render_template('add_skills.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/mysql', methods=['POST', 'GET'])
def nameWIP2():
    with sqlite3.connect('sql/skills.db') as con:
        cur = con.cursor()
        x = cur.execute("SELECT * from FUNCIONARIOS ")
        rows = x.fetchall()
        employees = [dict(id=row[0], nome=row[1], salario=row[2], cadastro=row[3]) for row in rows]
        con.commit()

        cur = con.cursor()
        x = cur.execute("SELECT * from PESSOAS")
        rows = x.fetchall()
        people = [dict(id=row[0], nome=row[1]) for row in rows]
        con.commit()

        # cur = con.cursor()
        # x = cur.execute("SELECT * from LANGUAGES")
        # rows = x.fetchall()
        # langs = [dict(nome_lingua=row[0], nota=row[1]) for row in rows]
        # con.commit()
        return render_template('MySQL.html', rec=people, rec2=employees, query='nenhuma')
    sqlite3.connect('sql/skills.db').close()
    return render_template('MySQL.html')

@app.route('/select', methods=['POST', 'GET'])
def select_from_tables():
    with sqlite3.connect('sql/skills.db') as con:
        cur = con.cursor()
        x = cur.execute(
            "SELECT * FROM PESSOAS WHERE nome = ?", [request.form['nome']]
        )
        rows = x.fetchall()
        people = [dict(id=row[0], nome=row[1]) for row in rows]
        x = cur.execute(
            "SELECT * FROM FUNCIONARIOS WHERE nome = ? OR salario = ?", [request.form['nome'], request.form['salario']]
        )
        rows = x.fetchall()
        employees = [dict(id=row[0], nome=row[1], salario=row[2]) for row in rows]
        con.commit()
        sqlite3.connect('sql/skills.db').close()
        return render_template('MySQL.html', rec=people, rec2=employees, query='select')

@app.route('/join', methods=['POST', 'GET'])
def join_from_tables():
    if request.method == 'GET':
        return render_template('MySQL.html', query='nenhuma')
    else:
        with sqlite3.connect('sql/skills.db') as con:
            cur = con.cursor()
            if request.form['nome'] != '':
                x = cur.execute("SELECT PESSOAS.nome, FUNCIONARIOS.salario, FUNCIONARIOS.cadastro FROM PESSOAS INNER JOIN FUNCIONARIOS"
                                " ON PESSOAS.nome = FUNCIONARIOS.nome AND PESSOAS.nome = ?", [request.form['nome']])
                rows = x.fetchall()
                result = [dict(nome=rows[0][0], salario=row[1], cadastro=row[2]) for row in rows]
            elif request.form['salario'] != '':
                x = cur.execute(
                    "SELECT PESSOAS.nome, FUNCIONARIOS.salario, FUNCIONARIOS.cadastro FROM PESSOAS INNER JOIN FUNCIONARIOS"
                    " ON PESSOAS.nome = FUNCIONARIOS.nome AND FUNCIONARIOS.salario = ?", [request.form['salario']])
                rows = x.fetchall()
                result = [dict(nome=rows[0][0], salario=row[1], cadastro=row[2]) for row in rows]
            else:
                x = cur.execute(
                    "SELECT PESSOAS.nome, FUNCIONARIOS.salario, FUNCIONARIOS.cadastro FROM PESSOAS INNER JOIN FUNCIONARIOS"
                    " ON PESSOAS.nome = FUNCIONARIOS.nome")
                rows = x.fetchall()
                size = len(rows)
                nome = []
                salario = []
                cadastro = []
                print(rows)
                for r in rows:
                    nome.append(r[0])
                    salario.append(r[1])
                    cadastro.append(r[2])
                result = [dict(nome=nome[i], salario=salario[i], cadastro=cadastro[i]) for i in range(size)]
            return render_template('MySQL.html', rec=result, query='join')
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


if __name__ == '__main__':
    app.run(debug=True)

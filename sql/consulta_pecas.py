import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.cursor()

x = cursor.execute("SELECT PESSOAS.nome, FUNCIONARIOS.cadastro FROM PESSOAS LEFT JOIN FUNCIONARIOS"
                   " ON FUNCIONARIOS.nome = PESSOAS.nome")
rows = x.fetchall()

print(rows)


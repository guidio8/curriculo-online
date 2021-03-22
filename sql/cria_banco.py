import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS SKILLS (nome_skill TEXT PRIMARY KEY, nota INT)"""
)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS ESTUDOS (lugar TEXT PRIMARY KEY, ano TEXT, tipo TEXT)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS LANGUAGES (nome_lingua TEXT PRIMARY KEY, nota INT)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS PESSOAS (id integer PRIMARY KEY, nome TEXT)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS FUNCIONARIOS (id_func integer PRIMARY KEY NOT NULL, nome TEXT, salario DOUBLE, cadastro integer)"""
)




import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.cursor()
cursor.execute(
    "REPLACE INTO ESTUDOS VALUES('Universidade Federal de São João del-Rei', '2015-2021', 'Bacharelado em Ciência da Computação')")
cursor.execute(
    "REPLACE INTO ESTUDOS VALUES('Colégio Franciscano Nossa Senhora Aparecida', '2010-2013', 'Ensino Médio')")

cursor.execute("REPLACE INTO SKILLS VALUES('Python', 9)")
cursor.execute("REPLACE INTO SKILLS VALUES('JAVA', 8)")
cursor.execute("REPLACE INTO SKILLS VALUES('HTML', 5)")
cursor.execute("REPLACE INTO SKILLS VALUES('MySQL', 9)")
cursor.execute("REPLACE INTO SKILLS VALUES('C++', 7)")
cursor.execute("REPLACE INTO SKILLS VALUES('C#', 8)")
cursor.execute("REPLACE INTO SKILLS VALUES('C', 9)")
cursor.execute("REPLACE INTO SKILLS VALUES('Excel', 7)")
cursor.execute("REPLACE INTO SKILLS VALUES('R', 6)")
cursor.execute("REPLACE INTO SKILLS VALUES('Assembly', 6)")

cursor.execute("REPLACE INTO LANGUAGES VALUES('English', 9)")
cursor.execute("REPLACE INTO LANGUAGES VALUES('Português', 10)")

cursor.execute("REPLACE INTO PESSOAS (nome) VALUES('Miguel')")
cursor.execute("REPLACE INTO PESSOAS (nome) VALUES('Maria Eduarda')")
cursor.execute("REPLACE INTO PESSOAS (nome) VALUES('Arthur')")
cursor.execute("REPLACE INTO PESSOAS (nome) VALUES('Davi')")
cursor.execute("REPLACE INTO PESSOAS (nome) VALUES('Gabriel')")

cursor.execute("REPLACE INTO FUNCIONARIOS (nome, salario, cadastro) VALUES('Miguel', 50000, 2578)")
cursor.execute("REPLACE INTO FUNCIONARIOS (nome, salario, cadastro) VALUES('Roberto', 50000, 26078)")
cursor.execute("REPLACE INTO FUNCIONARIOS (nome, salario, cadastro) VALUES('Maria Eduarda', 90000, 894512)")
cursor.execute("REPLACE INTO FUNCIONARIOS (nome, salario, cadastro) VALUES('Alice', 100000, 96203)")

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.cursor()

x = cursor.execute("SELECT * from SKILLS WHERE nome_skill = ''")
rows = x.fetchall()

print(rows)


import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.cursor()

cursor.execute("""DROP TABLE estudos""")
cursor.execute("""DROP TABLE SKILLS""")
cursor.execute("""DROP TABLE LANGUAGES""")

cursor.execute("""DROP TABLE PESSOAS""")
cursor.execute("""DROP TABLE FUNCIONARIOS""")


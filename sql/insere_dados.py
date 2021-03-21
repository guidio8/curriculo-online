import sqlite3

conn = sqlite3.connect('skills.db')

cursor = conn.cursor()
cursor.execute("""REPLACE INTO ESTUDOS VALUES('Universidade Federal de São João del-Rei', '2015-2021', 'Bacharelado')""")
cursor.execute("""REPLACE INTO ESTUDOS VALUES('Colégio Franciscano Nossa Senhora Aparecida', '2010-2013', 'Ensino Médio')""")

cursor.execute("""REPLACE INTO SKILLS VALUES('Python', 9)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('JAVA', 8)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('Website Making', 5)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('MySQL', 9)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('C++', 7)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('C#', 8)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('C', 9)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('Excel', 7)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('R', 6)""")
cursor.execute("""REPLACE INTO SKILLS VALUES('Assemply', 6)""")

cursor.execute("""REPLACE INTO LANGUAGES VALUES('English', 9)""")
cursor.execute("""REPLACE INTO LANGUAGES VALUES('Português', 8)""")


conn.commit()
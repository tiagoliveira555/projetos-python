import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")

cursor.execute("INSERT INTO pessoas VALUES('Tiago',35,'tiagoliveira555@gmail.com')")

banco.commit()

#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

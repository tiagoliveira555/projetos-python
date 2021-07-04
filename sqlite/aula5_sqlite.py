import sqlite3

nome = 'Juliana'
idade = 28
email = 'juliana@gmail.com'

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")

#cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"')")

cursor.execute("UPDATE pessoas SET nome = 'Fabio' WHERE idade = 28")

banco.commit()

#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

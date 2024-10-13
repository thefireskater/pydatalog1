from pyDatalog import pyDatalog
import sqlite3

# Symbols have to be declared ("bound")
pyDatalog.create_terms('X,Y,Z,manager,works_in')

# Facts, called literals, are preceded by a +
+ manager('Rick', 'Darwin')
+ manager('Barmak', 'Rick')
+ works_in('Rick', 'Engineering')
+ works_in('Darwin', 'Engineering')

manager(X, Z) <= manager(X, Y) & manager(Y, Z)

print('X works in engineering')
print(works_in(X, 'Engineering'))
print()

print('X manages Y')
print(manager(X, Y))

# creates a db if a db of this name doesn't exist
connection = sqlite3.connect(':memory:')
print(connection.total_changes) # ensure that the connection was successful

cursor = connection.cursor()
cursor.execute('CREATE TABLE person (name TEXT, age INTEGER)')
cursor.execute("INSERT INTO person VALUES ('Alice', 30)")
cursor.execute("INSERT INTO person VALUES ('Bob', 31)")

rows = cursor.execute("SELECT name FROM person WHERE age < 31").fetchall()
print(rows)

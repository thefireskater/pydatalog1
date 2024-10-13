from pyDatalog import pyDatalog

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

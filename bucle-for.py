frutas = ['manzanas', 'peras', 'mangos']
for fruta in frutas:
    print(fruta)

iter('cadena')
print(iter('cadena'))
iter(['a','b','c'])
print(iter(['a','b','c']))
iter(('a','b','c'))
print(iter(('a','b','c')))
iter({'a','b','c'})
print(iter({'a','b','c'}))
iter({'a':1,'b':2,'c':3})
print(iter({'a':1,'b':2,'c':3}))

iterador = iter(frutas)
print(next(iterador)) # manzanas
print(next(iterador)) # peras
print(next(iterador)) # mangos
# print(next(iterador)) # error ya q no existe mas elementos

# DICCIONARIOS ITERADOR
estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4
}
print(estudiantes)
# ===> itera las llaves
for estudiante in estudiantes:
    print(estudiante)
    # print(estudiantes[estudiante])

# ===> itera las llaves .keys()
for estudiante in estudiantes.keys():
    print(estudiante)

# ===> itera los valores .values()
for estudiante in estudiantes.values():
    print(estudiante)

# ===> itera en una tupla los llaves y valores .items()
for estudiante in estudiantes.items():
    print(estudiante)
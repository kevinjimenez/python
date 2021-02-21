# range(comienzo, fin, pasos)
# no incluye el final
my_range = range(1,5)
print(type(my_range))
for i in my_range:
    print(i)

my_range = range(0, 7, 2)
my_oyher_range = range(0, 8, 2)

print(my_range == my_oyher_range) # misma secuencia de valores

for i in my_range:
    print(i)

for i in my_oyher_range:
    print(i)

print(id(my_range))
print(id(my_oyher_range))

# Object equality => igualdad de objetos operador (is)
print(my_range is my_oyher_range)

for i in  range(0, 101, 2):
    print(i)

# numeros nones (impares)
for i in  range(1, 100, 2):
    print(i)
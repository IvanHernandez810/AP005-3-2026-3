my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
print(my_lista)
print(type(my_lista))
print(my_lista[2])
print(len(my_lista))
print(my_lista[0:2])

my_lista.append('Blanco')
my_lista.insert(3, 'Negro')
my_lista.extend(['Marron', 'Gris'])
print(my_lista)

print(my_lista.index('Azul'))
my_lista.remove('Marron')
my_lista.insert(8, 'Marron')
print(my_lista.pop())
print(my_lista)

my_lista_3 = my_lista * 3
print(my_lista_3)

my_lista_ordenada = sorted(my_lista)
print(my_lista_ordenada)

my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
my_NumList.sort()
print(my_NumList)
my_NumList.sort(reverse=True)
print(my_NumList)

my_tupla = tuple(my_lista)
print(my_tupla)
print(my_tupla[0], my_tupla[2])
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

my_tupla_unitaria = ('Blanco',)
print(my_tupla_unitaria)

my_tupla2 = 'Gaspar', 5, 8, 1999
nombre, dia, mes, anio = my_tupla2
print(nombre, dia, mes, anio)

my_lista2 = list(my_tupla2)
print(my_lista2)

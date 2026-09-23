# Crea una lista de colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
# Imprime la lista llamada my_lista
print(my_lista)
# Imprime el tipo de la variable my_lista
print(type(my_lista))
# Imprime el string que está en la posición 2
print(my_lista[2])

# Cuenta la cantidad de elementos de la lista
print("my_lista size: ", len(my_lista))
# Imprime desde el inicio de la lista hasta la posición 2, sin incluirla
print(my_lista[0:2])
# Hace lo mismo que arriba, pero con una forma más corta de escribirlo
print(my_lista[:2])

# .append agrega un elemento al final de la lista
my_lista.append('Blanco')
# Imprime la lista con el nuevo elemento
print(my_lista)

# .insert mete el elemento en el índice 3, sin borrar nada; empuja lo demás hacia adelante
my_lista.insert(3, 'Negro')
# Imprime la lista con el nuevo elemento
print(my_lista)

# .extend agrega varios elementos al final de la lista, de otra lista
my_lista.extend(['Marron', 'Gris'])
# Imprime la lista con los nuevos elementos
print(my_lista)

# .index dice en qué posición está el elemento dentro de la lista
print(my_lista.index('Azul'))

# .remove elimina el primer elemento que coincide con el valor dado
my_lista.remove('Marron')
# Imprime la lista sin el elemento removido
print(my_lista)

# Vuelve a insertar 'Marron', ahora en la posición 8
my_lista.insert(8, 'Marron')
# Imprime la lista con el elemento reinsertado
print(my_lista)

# .pop() sin argumento elimina el ÚLTIMO elemento y lo devuelve; print lo muestra
print(my_lista.pop())
# Mide cuántos elementos quedan en my_lista
size = len(my_lista)
# Imprime "size = " y el número de elementos
print("size = ", size)

# Repite el contenido de la lista 3 veces seguidas y crea una lista nueva
my_lista_3 = my_lista * 3
# Imprime la lista repetida
print("my_lista_3: ", my_lista_3)

# Imprime un título
print("Sort:")
# Salto de línea
print()
# sorted() ordena alfabéticamente SIN modificar la lista original, y devuelve una lista nueva
my_lista_ordenada = sorted(my_lista)
# Imprime la lista nueva ya ordenada
print(my_lista_ordenada)

# Crea una lista de números desordenada
my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Imprime un título
print("Ordering my_NumList: ")
# .sort() ordena la lista de menor a mayor, modificándola directamente (no devuelve nada útil)
my_NumList.sort()
# Imprime la lista ya ordenada de menor a mayor
print(my_NumList)

# .sort(reverse=True) ordena la lista, pero de mayor a menor
my_NumList.sort(reverse=True)
# Imprime la lista ordenada de mayor a menor
print("De mayor a menor: ", my_NumList)


# Imprime una línea decorativa
print("###########################")
# Imprime una línea decorativa
print("###########################")
# Imprime una línea decorativa
print("###########################")
# Imprime el título de esta sección
print("############TUPLAS#########")
# tuple() convierte la lista en una tupla: una copia que ya no se puede modificar
my_tupla = tuple(my_lista)
# Salto de línea
print()
# Salto de línea
print()
# Imprime la tupla recién creada
print("my_tuple: ", my_tupla)

# Imprime lo que hay en la posición 0 de la tupla
print(my_tupla[0])
# Imprime lo que hay en la posición 2 de la tupla
print(my_tupla[2])

# in revisa si 'Rojo' está dentro de la tupla; devuelve True o False
print('Rojo' in my_tupla)
# .count cuenta cuántas veces aparece 'Rojo' en la tupla
print(my_tupla.count('Rojo'))

# La coma después del valor es obligatoria para que Python lo trate como tupla de un solo elemento
my_tupla_unitaria = ('Blanco',)
# Imprime la tupla de un solo elemento
print(my_tupla_unitaria)

# Se pueden crear tuplas sin paréntesis, separando los valores solo con comas
my_tupla = 'Gaspar', 5, 8, 1999
# Imprime la tupla completa
print(my_tupla)

# Desempaquetado: cada valor de la tupla se guarda en una variable, en el mismo orden
nombre, dia, mes, anio = my_tupla
# Imprime el nombre
print(nombre)
# Imprime el día
print(dia)
# Imprime el mes
print(mes)
# Imprime el año
print(anio)

# Imprime todos los datos juntos, con etiquetas
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", anio)

# list() convierte la tupla en una lista, que sí se puede modificar
my_lista2 = list(my_tupla)
# Imprime la nueva lista
print(my_lista2)

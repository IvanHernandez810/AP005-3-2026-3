# Lista con los nombres de las canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# Lista con la cantidad de reproducciones de cada canción, en el mismo orden que songs
playcounts = [78, 29, 44, 21, 89, 5]

# Crea un diccionario vacío donde vamos a guardar canción: reproducciones
plays = {}
# Recorre cada posición (0,1,2...) de las listas, ya que las dos tienen el mismo tamaño
for i in range(len(songs)):
    # Guarda el nombre de la canción en la posición i
    nombre_cancion = songs[i]
    # Guarda el número de reproducciones en la posición i
    numero_de_veces = playcounts[i]
    # Agrega la pareja clave:valor al diccionario plays
    plays[nombre_cancion] = numero_de_veces

# Imprime el diccionario ya armado
print(plays)

# Agrega una clave nueva "Purple Haze" con valor 1
plays["Purple Haze"] = 1
# Cambia el valor de la clave "Respect", que ya existía, de 89 a 94
plays["Respect"] = 94
# Imprime "After: " y el diccionario actualizado
print("After: ", plays)

# Crea un diccionario vacío para guardar listas de canciones (playlists)
library = {}
# Guarda el diccionario plays bajo la clave "The Best Songs"
library["The Best Songs"] = plays
# Crea otra clave "Sunday Feelings" con un diccionario vacío como valor
library["Sunday Feelings"] = {}
# Imprime library, que contiene un diccionario dentro de otro diccionario
print(library)

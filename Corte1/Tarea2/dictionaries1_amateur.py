songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {}
for i in range(len(songs)):
    nombre_cancion = songs[i]
    numero_de_veces = playcounts[i]
    plays[nombre_cancion] = numero_de_veces

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94
print("After: ", plays)

library = {}
library["The Best Songs"] = plays
library["Sunday Feelings"] = {}
print(library)

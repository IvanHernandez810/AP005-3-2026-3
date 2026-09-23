# Diccionario con la altura de algunos edificios
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Ping An": 599}

# .get() busca la clave de forma segura, sin romper el programa si no existe
altura = building_heights.get("Shanghai Tower")
# Imprime 632, porque "Shanghai Tower" sí existe en el diccionario
print(altura)

# Busca una clave que NO existe en el diccionario
altura_2 = building_heights.get("My House")
# Imprime None, porque .get() no rompe el programa, solo devuelve None si no encuentra la clave
print(altura_2)

# Diccionario donde las claves son números de boleto y los valores son premios
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket"}

# .pop() elimina la clave 320291 del diccionario y devuelve su valor; si no existiera, devolvería "No Prize"
premio = raffle.pop(320291, "No Prize")
# Imprime "Gift Basket", el premio que fue eliminado
print(premio)
# Imprime el diccionario raffle ya sin la clave 320291
print(raffle)

# Diccionario con las notas de dos estudiantes
test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81]}

# .keys() da todas las claves del diccionario; list() las convierte en una lista
nombres = list(test_scores.keys())
# Imprime la lista de nombres de estudiantes
print(nombres)

# .values() da todos los valores del diccionario; list() los convierte en una lista
notas = list(test_scores.values())
# Imprime la lista de listas de notas
print(notas)

# Recorre el diccionario; al iterar directo sobre un diccionario, se recorren sus claves
for student in test_scores:
    # Usa la clave actual (student) para obtener su valor asociado
    scores = test_scores[student]
    # Imprime el nombre del estudiante junto con sus notas
    print(student, scores)

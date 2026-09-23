building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Ping An": 599}

altura = building_heights.get("Shanghai Tower")
print(altura)

altura_2 = building_heights.get("My House")
print(altura_2)

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket"}

premio = raffle.pop(320291, "No Prize")
print(premio)
print(raffle)

test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81]}

nombres = list(test_scores.keys())
print(nombres)

notas = list(test_scores.values())
print(notas)

for student in test_scores:
    scores = test_scores[student]
    print(student, scores)

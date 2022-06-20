import random
dict = {
        "51.90085164360474, -2.05449667652761": 285,
        "51.905367372524125, -2.0598744141647347": 20,
        "51.90379881573086, -2.1148557115609115": 185,
    }

coordinates = random.choice(list(dict.keys()))
bearing = dict[coordinates]

bearingguess = 180

if int(bearingguess) >= (bearing - 15) and int(bearingguess) <= (bearing + 15):
    print('win', bearing)
else:
    print('lose', bearing)

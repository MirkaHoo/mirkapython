import random
oikea_luku= random.randint(1,10)
while True:
    try:
        arvaus = int(input("arvaa luku 1-10: "))
        if arvaus < oikea_luku:
            print("liian pieni")
        if arvaus > oikea_luku:
            print("liian suuri")
        else:
            print("oikein!")
            break
    except ValueError:
        print("syötä vain kokonaisluku.")
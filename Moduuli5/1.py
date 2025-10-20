#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.



import random
luku = int(input("anna arpakuutioiden maara:"))
summa = 0
for _ in range(luku):
    arpakuutio = random.randint(1,6)
    summa += arpakuutio
print(f"arpakuutioiden summa: {summa}")

#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random
def noppa():
    silmaluku = random.randint(1,6)
    return silmaluku

tulos = 0
while tulos != 6:
    tulos = noppa()
    print("tulos:", tulos)



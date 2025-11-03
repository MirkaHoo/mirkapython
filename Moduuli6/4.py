#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laske_yhteen(kokonaisluvut):
    summa = sum(kokonaisluvut)
    return summa

kokonaisluvut = [ 2, 4, 6, 8, 10, 12, 14, 16]
tulos = laske_yhteen(kokonaisluvut)
print("summa on:", tulos)
#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
#joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
def noppa(maara):
    silmaluku = random.randint(1,maara)
    return silmaluku

maarat = int(input("anna maara: "))
tulos = 0
while tulos != maarat:
    tulos = noppa(maarat)
    print("tulos:", tulos)
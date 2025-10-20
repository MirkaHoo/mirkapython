#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes
# tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []
while True:
    luku = input("anna luku: ")
    if luku =="":
        print("loppu.")
        break
    try:
        luku = int(luku)
        luvut.append(int(luku))
    except ValueError:
        print("yritä uudelleen.")
luvut.sort(reverse=True)
print("viisi suurinta lukua")
for luku in luvut[:5]:
    print(luku)



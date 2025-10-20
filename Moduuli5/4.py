#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen)
# ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []
for i in range(5):
    nimi = input("anna kaupunki:")
    kaupungit.append(nimi)
print("\nviisi kaupunkia:")
for kaupunki in kaupungit:
    print(kaupunki)

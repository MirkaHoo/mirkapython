#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän.

# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

#funktio->parametri:gallona
def bensiini_litra(gallona):
    litra = gallona * 3.785
    return litra
#return, palauttaa pääohjelmaan

gallona = float(input("anna gallonat:"))
litroina = bensiini_litra(gallona)
print(f"{gallona} gallona on {litroina:.2f} litraa.")

#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.


pituus = int(input("kuhan pituus sentteinä: "))
alamitta = 37
if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"kuha on alamittainen, laske kuha takaisin järveen. pituutta puuttuu {puuttuu} cm.")
else:
    print("kuha on lain sallimissa mitoissa. voidaan pitää. ")

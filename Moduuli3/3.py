#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.


sukupuoli = input("anna sukupuolesi (nainen/mies):" ).strip().lower()
hemoglobiini = int(input("anna hemoglobiinisi (g/l). "))

if sukupuoli == 'nainen':
    if hemoglobiini < 117:
        print("hemoglobiinisi on alhainen.")
    elif hemoglobiini <= 175:
        print("hemoglobiinisi on normaali.")
    else:
        print("hemoglobiinisi on korkea.")

    print
if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("hemoglobiinisi on alhainen.")
    elif hemoglobiini <= 195:
        print("hemoglobiinisi on normaali.")
    else:
        print("hemoglobiinisi on korkea.")
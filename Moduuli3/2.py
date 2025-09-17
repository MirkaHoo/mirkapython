#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen
# alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.



hyttiluokka = input("anna hyttiluokkasi: ")
if hyttiluokka == 'LUX' or 'lux':
    print("parvekkeellinen hytti yläkannella. ")
elif hyttiluokka == 'A' or 'a' :
    print("ikkunallinen hytti autokannen yläpuolella. ")
elif hyttiluokka == 'B' or 'b' :
    print("ikkunaton hytti autokannen yläpuolella. ")
elif hyttiluokka == 'C' or 'c' :
    print("ikkunaton hytti autokannen alapuolella. ")
else:
    print("virheellinen hyttiluokka. ")

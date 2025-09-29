oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
max_yritykset = 5
while yritykset < max_yritykset:
    tunnus = input("anna käyttäjätunnus:")
    salasana = input("anna salasana:")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print("väärä tunnus tai salasana.\n")
    if yritykset == max_yritykset:
        print("pääsy evätty.")

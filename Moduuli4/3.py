luvut = []
while True:
    luku = input("anna luku (enter lopettaa): ")
    if luku =="":
        break
    try:
        luku = float(luku)
        luvut.append(luku)
    except ValueError:
        print("virheellinen luku, yritä uudelleen.")
    if luvut:
        print(f"pienin luku: {min(luvut)}")
        print(f"suurin luku: {max(luvut)}")
    else:
        print("et antanut lukua.")
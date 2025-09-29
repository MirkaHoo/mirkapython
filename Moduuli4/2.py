while True:
    tuuma = float(input("anna tuumamäärä (neg.lopettaa):"))
    if tuuma < 0:
        print("ohjelma lopettaa.")
        break
    sentit = tuuma * 2.54
    print(f"{tuuma} tuumaa on {sentit:.2f} senttimetriä.\n")
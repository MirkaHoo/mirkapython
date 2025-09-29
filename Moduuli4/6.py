import random
def laske_pii_likiarvo(pisteiden_maara):
    ympyrassa =  0
    for _ in range(pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            ympyrassa += 1
    pii_likiarvo = 4 * ympyrassa / pisteiden_maara
    return pii_likiarvo
def main():
    try:
        pisteet = int(input("anna pisteiden määrä:"))
        if pisteet <= 0:
            print("pisteden määrän täytyy olla positiivinen.")
            return
        pii_likiarvo = laske_pii_likiarvo(pisteet)
        print(f"piin likiarvo {pisteet} pisteellä on noin: {pii_likiarvo}")
    except ValueError:
        print("syötteen täytyy olla kokonaisluku.")
if __name__ == "__main__":
        main()
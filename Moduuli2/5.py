leiviska = int(input("anna leiviskoiden maara: "))
naulat = int(input("anna naulojen maara: "))
luodit = float(input("anna luotien maara: "))
luodit = leiviska*20*32+naulat*32+luodit
grammat = luodit*13.3
kilot = int(grammat //1000)
yli = grammat % 1000
print(f"paino on {kilot} kg {yli:.2f} g")

temperatura=float(input("Qual a temperatura? "))

if (temperatura >= 30 and temperatura <= 40):
    print("leve agua gelada")
elif (temperatura >= 20 and temperatura <= 40):
    print("O clima está ameno")
elif (temperatura <20):
    print("Leve uma Blusa")
elif (temperatura >40):
    print("Não saia sem protetor")
else:
    print("")
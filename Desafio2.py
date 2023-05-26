Peso=float(input("Qual seu peso? responda em KG: "))
Altura=float(input("Qual sea altura? responda em metros: "))

calculo = Peso/(Altura*Altura)

if (calculo <18.5):
    print("abaixo do peso")
elif (calculo >=18 and calculo <25):
    print("Peso na media")
elif (calculo >=25 and calculo <30):
    print("excesso de peso")
elif (calculo >=30 and calculo < 35):
    print("obesidade I")
elif (calculo >=35 and calculo <=40):
    print("obesidade II")
else:
    print("Obesidade III")
N1 = float(input(f"\033[35m Ano que você nasceu: \033[m"))
N2 = float(input(f"\033[35m Ano atual: \033[m"))

idade = (N2 - N1)
print(f'\033[35m Sua idade: {idade}\033[m')

if idade >= 18:
    print(f'\033[35m Você é: +18 \033[m')
else:
    print(f'\033[35m Você é: -18 \033[m')

print(f'\033[35m Lucas e Jansen Melhores professores do Senai\033[m')

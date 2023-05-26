N1 = float(input(f"\033[35m nota 1: \033[m").replace(',','.         '))
N2 = float(input(f"\033[35m nota 2: \033[m").replace(',','.         '))
N3 = float(input(f"\033[35m nota 3: \033[m").replace(',','.         '))
N4 = float(input(f"\033[35m nota 4: \033[m").replace(',','.         '))

Soma = (N1 + N2 + N3 + N4)

Média = (Soma / 4)

print(f'\033[35m Média final: {Média}\033[m')
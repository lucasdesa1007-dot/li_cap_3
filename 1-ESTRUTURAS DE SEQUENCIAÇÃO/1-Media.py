import math as mat

numeros = [float(input(f"Digite o {i}º número: ")) for i in range(1, 6)]
media = mat.fsum(numeros) / 5
print(f"A média dos cinco números é {media:.2f}")

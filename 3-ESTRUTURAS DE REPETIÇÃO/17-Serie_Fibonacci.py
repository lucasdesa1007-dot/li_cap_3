num1 = int(input("Digite o primeiro termo: "))
num2 = int(input("Digite o segundo termo: "))

serie = [num1, num2]

for _ in range(18):
    serie.append(serie[-1] + serie[-2])

print(serie)

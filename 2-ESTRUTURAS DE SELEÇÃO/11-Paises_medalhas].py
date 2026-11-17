
paises = []

for i in range(1, 4):
    print(f"\n--- {i}º PAÍS ---")

    nome = input("Nome do país: ")
    ouro = int(input("Medalhas de ouro: "))
    prata = int(input("Medalhas de prata: "))
    bronze = int(input("Medalhas de bronze: "))

    pontos = (ouro * 3) + (prata * 2) + bronze

    paises.append([nome, pontos])

paises.sort(key=lambda pais: pais[1], reverse=True)

print("\nCLASSIFICAÇÃO OLÍMPICA")

for i in range(3):
    print(f"{i + 1}º lugar: {paises[i][0]} - {paises[i][1]} pontos")

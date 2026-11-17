capacidade = float(input("Capacidade do tanque (litros): "))
litros_abastecidos = float(input("Litros abastecidos: "))
quilometros = float(
    input("Quilômetros percorridos desde o último abastecimento: "))

if capacidade <= 0 or litros_abastecidos <= 0 or litros_abastecidos > capacidade or quilometros < 0:
    print("Valores inválidos.")

else:
    consumo = quilometros / litros_abastecidos
    litros_restantes = capacidade - litros_abastecidos
    autonomia = litros_restantes * consumo

    print(f"Consumo médio: {consumo:.2f} km/l")
    print(f"Autonomia antes do abastecimento: {autonomia:.2f} km")

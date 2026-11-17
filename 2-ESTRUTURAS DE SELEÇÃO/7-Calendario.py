import calendar as cal
import locale as loc

try:
    loc.setlocale(loc.LC_TIME, 'pt_BR.UTF-8')
    mes = int(input("Digite um número de 1 a 12: "))

    if mes >= 1 and mes <= 12:
        nome_mes = cal.month_name[mes]
        print(f"Mês: {nome_mes}")
except ValueError as erro:
    print(f"Erro: {erro}")

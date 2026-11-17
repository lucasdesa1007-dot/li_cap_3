
import datetime as dt

dia_nasc = int(input("Dia do nascimento: "))
mes_nasc = int(input("Mês do nascimento: "))
ano_nasc = int(input("Ano do nascimento: "))

dia_atual = int(input("Dia atual: "))
mes_atual = int(input("Mês atual: "))
ano_atual = int(input("Ano atual: "))

nascimento = dt.date(ano_nasc, mes_nasc, dia_nasc)
atual = dt.date(ano_atual, mes_atual, dia_atual)

if nascimento > atual:
    print("Data de nascimento inválida.")

else:
    anos = ano_atual - ano_nasc
    meses = mes_atual - mes_nasc
    dias = dia_atual - dia_nasc

    if dias < 0:
        meses -= 1
        mes_anterior = mes_atual - 1

        if mes_anterior == 0:
            mes_anterior = 12

        ano = ano_atual

        if mes_atual == 1:
            ano -= 1

        dias_mes = (dt.date(ano, mes_atual, 1) -
                    dt.date(ano, mes_anterior, 1)).days

        dias += dias_mes

    if meses < 0:
        anos -= 1
        meses += 12

    print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")

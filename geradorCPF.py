import random
import sys

for _ in range(1):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regr_1 = 10

    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regr_1
        contador_regr_1 -= 1
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regr_2 = 11

    resultado_2 = 0
    for numero in dez_digitos:
        resultado_2 += int(numero) * contador_regr_2
        contador_regr_2 -= 1
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_recebido = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_recebido)
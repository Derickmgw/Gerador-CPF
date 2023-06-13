'''
CPF: 813.323.780-72
Coleta a soma dos 9 primeiros dígitos do Cpf
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

ex.: 813.323.780-72 (81332378072)
    10  9  8  7  6  5  4  3  2 
    8   1  3  3  2  3  7  8  0
    80  9 24 21 12 15 28 24  0

soma todos os resultados:
80 + 9 + 24 + 21 + 12 + 15 + 28 + 24 + 0 = 213
Multiplicar o resultado anterior por 10
213 * 10 = 2130
Obter o resto da divisão da conta anterior por 11
2130 % 11 = 7
se o resultado anterior for maior que nove:
    resultado é 0
contrario disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

para o segundo digito fazemos o memso calculo, so que  na parte 
da multiplicação icluimos o primeiro digito e fazemos uma contagem
regressiva a partir do 11:

ex.: 813.323.780-72 (81332378072)
   11  10  9  8  7  6  5  4  3  2 
    8   1  3  3  2  3  7  8  0  7
    80  9 24 21 12 15 28 24  0 14

Somar todos os valores:
80 + 9 + 24 + 21 + 12 + 15 + 28 + 24 + 0 + 14 = 227
Multiplicar o resultado anterior por 10
227 * 10 = 2227
Obter o resto da divisão da conta anterior por 11
2227 % 11 = 2
se o resultado anterior for maior que nove:
    resultado é 0
contrario disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 2

'''
import re
import sys
entrada = input('Digite seu CPF: ')
cpf_enviado = re.sub(r'[^0-9]','',
entrada)

entrada_sequencial = \
cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()
    
nove_digitos = cpf_enviado[:9]
contador_regr_1 = 10
contador_regr_2 = 11

resultado_1 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regr_1
    contador_regr_1 -= 1
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print('Primeiro dígito =', digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regr_2 = 11

resultado_2 = 0
for numero in dez_digitos:
    resultado_2 += int(numero) * contador_regr_2
    contador_regr_2 -= 1
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print('Segundo dígito =', digito_2)

cpf_recebido = f'{nove_digitos}{digito_1}{digito_2}'
print(f'CPF gerado foi: {cpf_recebido}')

if cpf_enviado == cpf_recebido:
    print('CPF valido')
else:
    print('Cpf invalido')
    
    









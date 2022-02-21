"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numerointeiro = input('Digite um número inteiro: ')

if numerointeiro.isdigit():
    numerointeiro = int(numerointeiro)

    if numerointeiro % 2 == 0:
        print(f'{numerointeiro} é par')

    else:
        print(f'{numerointeiro} é ímpar')
else:
    print(f'{numerointeiro} não é um número inteiro')
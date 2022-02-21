"""
Operadores relacionais
== igualdade
> maior que
>= maior que ou igual
< menor que
<= menor que ou igual
!= diferente
(sempre que executado retornara um valor booleano)
= (afirmação)
== (pergunta)
"""
"""
print (2 == 2) #verifica a igualdade

num_1 = 2 #int
num_2 = 2 #int
expressao = (num_1 == num_2)

print(3 > 2) # > maior que
num_1 = 3 #int
num_2 = 2 #int
express = (num_1 > num_2)
"""

nome = input('Qual é o seu nome?')
idade = input('Qual é sua idade?')

idade = int(idade)

#limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} Pode pegar o empréstimo')
else:
    print(f'{nome} Não pode pegar o empréstimo')




















"""
Formatação de strings
"""

nome = 'Jéssica'
idade = 25
altura = 1.65
e_maior = idade > 18
peso = 90
imc = peso / altura ** 2


print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #exibe 2 casa decimais e 0 F é de ponto Flutuante.
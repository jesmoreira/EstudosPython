"""
- Criar variáveis para nome (str), idade (int)
- altura (float) e peso (float) de uma pessoa
- Criar variável com o ano atual (int)
- Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
-Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
- Exibir um texto com todos os valores na tela usando F-strings (com as chaves)
"""

nome = 'Jéssica'
idade = 26
altura = 1.65
peso = 90.0
anoatual = 2022
anodenas = anoatual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}')
print(f'o IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anodenas} ')
















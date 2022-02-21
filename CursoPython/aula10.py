"""
Operadores lógicos

and, or, not
in e not in

>> and (só retorna TRUE se as duas expressões forem verdadeiras
e caso 1 seja falsa retorna FALSE)
"""

"""
# verdadeiro e falso = false as 2 precisam ser verdadeiras para retornar true
comparacao1 and comparacao2

# no OR retorna TRUE se uma das expressões forem verdadeiras
comp1 or comp2

# a expressão NOT é de inversão

a = ''
b = 0

if not a:
    print('por favor preencha o valor de a')
"""
"""
nome = 'Jéssica'
if 'l' in nome:
     print(f'existe a letra i em {nome}')
else:
     print(f'Não existe essa letra no nome {nome}')
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Jess'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
     print('Você está logado no sistema')
else:
     print('Usuário ou senha inválidos')


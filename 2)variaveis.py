# Comentário é feito com # ou ''' ''', como no exemplo abaixo:
#

"""
Este é um comentário de várias linhas
Isso ainda é um comentário
"""

# Variáveis são espaços na memória do computador que armazenam dados
# para serem utilizados pelo programa.
# Cada variável tem um nome e um tipo de dado.
# O nome da variável é uma referência para o espaço na memória.
# O tipo de dado é o tipo de dado que a variável armazena.
# O tipo de dado pode ser um número, uma string, uma lista, um dicionário, etc.
# >> O tipo de dado é definido quando a variável é criada.

# Operadores de Atribuição
# São operadores que atribuem valores a variáveis
# Exemplo: x = 10
# x = 10 é um operador de atribuição
# x é a variável
# 10 é o valor
# = é o operador de atribuição

# Em Python não é necessário declarar o tipo de dado da variável.
idade = 29 #Cria uma variável chamada idade e armazena o valor 26
print(idade) #Imprime o valor da variável idade
print('\n')

nome = 'César' #Cria uma variável chamada nome e armazena o valor 'César'
print(nome) #Imprime o valor da variável nome
print('\n')


"""
Tipos de variáveis:

1) int - inteiro, ou seja, sem decimal
2) float - números do conjunto real, ou seja, com decimal
3) str - string, cadeia de caracteres
4) bool - booleano, True(1) ou False (0)
5) list - lista
6) dict - dicionário
"""


idade = 29
altura = 1.80
nome = 'César Espirandelli'
estudando = True
lista = []
dicionario = {}

print(idade, type(idade)) #Imprime o valor da variável idade e o tipo de dado
print(altura, type(altura)) #Imprime o valor da variável altura e o tipo de dado
print(nome, type(nome)) #Imprime o valor da variável nome e o tipo de dado
print(estudando, type(estudando)) #Imprime o valor da variável estudando e o tipo de dado
print(lista, type(lista)) #Imprime o valor da variável lista e o tipo de dado
print(dicionario, type(dicionario)) #Imprime o valor da variável dicionario e o tipo de dado


# Obtendo dados do usuários e armazenando em variáveis
linguagem = input('Qual é a linguagem de programação que você está estudando? ')
print('Você está estudando', linguagem)
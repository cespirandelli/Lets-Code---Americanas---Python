# Como realizar conversões de tipos de dados?
# Caso queira transformar um valor de um tipo de dado em outro tipo de dado, 
# basta utilizar as funções de conversão de tipos de dados.

'''
# Funções de conversão de tipos de dados
# int() - converte para inteiro
# float() - converte para float
# str() - converte para string
# bool() - converte para booleano
# list() - converte para lista
# dict() - converte para dicionário
'''

# Exemplo de conversão de tipos de dados
# idade = input('Digite sua idade: ') #Obtém a idade do usuário e armazena na variável idade
# idade = int(idade) #Converte a idade para inteiro
# print(idade, type(idade)) #Imprime o valor da variável idade e o tipo de dado


# CONVERSÃO DE TIPOS
idade = '26' # string
numero1 = '10' # string
numero2 = '20' #Cria uma variável do tipo string chamada numero2 e armazena o valor '20'

# Como Python é uma linguagem de tipagem forte, não é possível realizar operações aritméricas
# duas strings irão se concatenar ao invés de somar
#print(numero1 + numero2) # Imprime 1020

# Para realizar operações aritméticas com strings, é necessário converter os valores para inteiros
# ou para float
#print(int(numero1) + int(numero2)) # Imprime 30

print(idade, type(idade))
idade_inteira = int(idade)
print(idade_inteira, type(idade_inteira))

# Sempre que o usuário digitar algo no terminal, 
# o Python irá armazenar o valor como string, com a função input()

altura = input('Digite sua altura: ')
print(altura, type(altura)) #aqui temos uma string

# Para poder utilizar isso como outro tipo, convertemos diretamente no input()
altura = float(input('Digite sua altura: '))
print(altura, type(altura)) #agora temos um float

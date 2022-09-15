# Iremos tratar de outro controlador de fluxo
# O While é um laço de repetição que executa uma ação 
# enquanto uma condição for verdadeira

# Exemplo: enquanto a idade for menor que 18, o programa 
# deve imprimir a mensagem 'Menor de idade'
'''
idade = 0
while idade < 18:
    print('Idade: ', idade)
    print('Menor de idade')
    idade = idade + 1
print(idade, 'Maior de idade', sep=' -> ')
'''

# While é uma estrutura de laço condicional, usamos quando não sabemos
# quantas vezes será necessário realizar uma ação até que uma condição seja satisfeita

'''
    Sortear um número aleatório, enquanto o número sorteado for diferente do desejado
    o programa deve continuar sorteando.
    Quando o número sorteado for igual ao número desejado, o programa deve parar.


import random
numero_sorteado = random.randint(0,21)
#print(numero_sorteado)

numero_escolhido = int(input('Informe um número entre 0 e 20: '))

while numero_escolhido != numero_sorteado:
    print('\n')
    print('Ainda não acertou o número, tente novamente... Número digitado: ', numero_escolhido)
    numero_escolhido = int(input('Informe um número entre 0 e 20: '))
    print('\n')


print('Você acertou!! O número sorteado foi: ', numero_sorteado)
'''

# Podemos também utilizar uma estrutura controlada com while
# Com o auxílio de um contador, podemos enumerar os "passos"
# assim que atingir um objetivo, ele é interrompído

'''
    Criar um laço de repetição que irá rodar 5 vezes, enquanto ele não alcançar
    a repetição desejada, toda iteração somará +1 ao contador.
    Quando o contador for maior ou igual a 5 ele será suspenso.
'''

contador = 0 

while contador <5:
    print(contador)
    contador = contador+1
print('Contador é igual a 5!')
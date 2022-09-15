# Estrutura de controle de fluxo
# if, elif, else

# Agora quero estabelecer alguma condição para que
# o programa execute ou não uma determinada ação.

# Exemplo: Se a idade for maior que 18, então o programa
# deve imprimir a mensagem 'Maior de idade'

# A estrutura de controle de fluxo if tem a seguinte sintaxe:
# if (condição):
#     ação

# A condição é uma expressão que retorna True ou False
# Se a condição for True, o programa executa a ação
# Se a condição for False, o programa não executa a ação
# if (idade > 18):
#     print('Maior de idade')

# Existem dois tipos de estruturas de repetição:
# Laços de repetição (loops) e condicionais
# Laços de repetição são estruturas que repetem uma ação
# Condicionais são estruturas que executam uma ação se uma condição for verdadeira

# Vamos tratar da estrutura condicional:
#idade = int(input('Digite sua idade: '))
idade = 20 #para não ter que rodar o input toda vez, coloco o valor aqui

if idade >= 18: #Se a idade for maior ou igual a 18, então...
    print('Maior de idade\n') # note a identação de 4 espaços
else: # caso contrário...
    print('Menor de idade\n')

"""
    Imagine que você queira imprimir "Aprovada(o)" se a média for maior ou igual a 7.
    E "Reprovada(o)" se a média for menor que 7.
"""

# nota1 = 5
# nota2 = 5
# nota3 = 5
# nota4 = 4
# media = (nota1 + nota2 + nota3 + nota4)/4

'''
    também seria possível pedir diretamente a média para o usuário
    media = float(input('Digite sua média: '))
    dessa forma não teríamos que declarar ou pedir as variáveis que recebem
    os valores das notas
'''
media = float(input('Digite a média do aluno: '))
print('\n')
# neste caso só existem dois outputs possíveis
# se a pessoa passou ou não

# if media >= 7:
#     print("Sua média foi: ", media)
#     print("Aprovada(o)\n")
# else:
#     print("Sua média foi: ", media)
#     print("Reprovada(o)\n")

# Podemos criar também o caso de que se a pessoa tirou 5 ou mais,
# ela pode ir para "Recuperação"
'''
if media >= 7 :
    print("Sua média foi: ", media)
    print('Você foi aprovada(o)!!')
elif media >= 5:
    print("Sua média foi: ", media)
    print('Você está de recuperação!')
else:
    print("Sua média foi: ", media)
    print('Você foi reprovado :(')
'''

# Exemplo de operações conjuntas
# A pessoa precisa de dois critérios para ser aprovada
# média >= 7 e presença em aulas superior à 75%

presenca = float(input('Qual foi a presença do aluno ? (0 a 100) '))

if media >= 7 and presenca >= 75:
    print('Aprovada(o)!')
elif media >=5 and presenca >= 75:
    print('Recuperação')
else:
    print('Reprovada(o)')
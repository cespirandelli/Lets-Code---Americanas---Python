# Operadoções Matemáricas (Aritméticas)

'''
    +   Adição
    -   Subtração
    *   Multiplicação
    /   Divisão
    //  Divisão Inteira
    %   Resto da Divisão
    **  Potência
'''

numero1 = 10
numero2 = 20

print('1: Soma......................', numero1 + numero2)
print('2: Subtração.................', numero1 - numero2)
print('3: Multiplicação.............', numero1 * numero2)
print('4: Divisão...................', numero1 / numero2)
print('5: Divisão Intera............', numero1 // numero2) #Parte decimal é ignorada
print('6: Resto da Divisão "mod"....', 20 % 3) #Qual o resto da divisão de 20 por 3? 20 dividido por 3 é 6 com resto 2
print('7: Potência..................', 2 ** 3) #2 elevado a 3
print('8: Igualdade.................', numero1 == numero2) #Verifica se os valores são iguais
print('\n')

# Operadores BOOLEANOS
# São operadores que retornam um valor lógico (True ou False)
# São utilizados para comparações e ou testar condições
# São utilizados em estruturas de controle (if, while, for)
# São utilizados em expressões lógicas (and, or, not)
# São utilizados em expressões condicionais (if, elif, else)

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print('Operador booleano 1: ', idade1 > idade2)          # Verifica se idade1 é maior que idade2
print('Operador booleano 2: ', idade1 <= idade2)         # Verifica se idade1 é menor ou igual a idade2
print('Operador booleano 3: ', 'Python' == 'python')     # Verifica se as strings são iguais
print('Operador booleano 4: ', 'banana' != 'abacaxi')    # Verifica se as strings são diferentes
print('Operador booleano 5: ', altura1 >= altura2)       # Verifica se altura1 é maior ou igual a altura2
print('Operador booleano 6: ', altura2 > altura3) 

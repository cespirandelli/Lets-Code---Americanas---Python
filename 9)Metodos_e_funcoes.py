# Agora iremos tratar de métodos e funções

# Métodos são funções que pertencem a um objeto (lista, tupla, dicionário, etc)
# Ou seja, métodos são funções que estão associadas a uma variável (o que é chamado de objeto)
# Para mais informações estudar sobre programação orientada a objetos (Object Oriented Programming - OOP)
# Para mais informações de funções, estudar sobre programação funcional	
# Funções são funções que não pertencem a um objeto

'''
    Exemplos de métodos
    nome = 'João'
    print(nome.upper()) #".upper()"  Imprime o nome em letras maiúsculas
    #Resultado: JOÃO
    print(nome.lower()) #".lower()"  Imprime o nome em letras minúsculas
    #Resultado: joão
    print(nome.title()) #".title()"  Imprime o nome com a primeira letra maiúscula
    #Resultado: João
'''

'''
    Exemplo de função
    def soma(a, b):          #Cria uma função chamada soma que recebe dois parâmetros
        return a + b         #Retorna a soma dos dois parâmetros
    
    print(soma(10, 20))      #Imprime o resultado da função soma        #Resultado: 30
'''

# Funções são blocos de código que realizam uma tarefa específica
# Funções são úteis para não precisar repetir o mesmo código várias vezes
# Funções podem receber parâmetros e retornar valores
# Funções podem ser criadas por nós mesmos
# Funções podem ser criadas por bibliotecas
# Funções podem ser criadas por frameworks
# Funções podem ser criadas por bibliotecas de terceiros



# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]
print('Lista original:   ', lista)


# Adiciona um elemento no final da lista    
# Para adicionar um elemento no final da lista, utilizamos o método ".append()"
lista.append(7) #Adiciona o número 7 no final da lista
print('Depois do append: ',lista)                        # Resultado: [1, 3, 12, 8, 2, 7]


# Adiciona um elemento em uma posição específica da lista
lista.insert(0, 20) #Adiciona o número 20 na posição 0 da lista
print('Depois do insert: ',lista)                        # Resultado: [20, 1, 3, 12, 8, 2, 7]


# Adiciona uma lista em outra lista, junta duas listas
lista2 = [10, 11, 12]
lista.extend(lista2) #Adiciona a lista2 no final da lista
print('Depois do extend: ',lista)                        # Resultado: [20, 1, 3, 12, 8, 2, 7, 10, 11, 12]


# Agora iremos remover elementos de uma lista
# Para remover um elemento de uma lista, podemos utilizar o método ".pop()"
# O método ".pop()" remove o último elemento da lista e retorna o elemento removido
# O método ".pop()" também pode receber um parâmetro, que é a posição do elemento que queremos remover
lista.pop() #Remove o último elemento da lista
print('Depois do pop:    ',lista)                        # Resultado: [20, 1, 3, 12, 8, 2, 7, 10, 11]
lista.pop(0) #Remove o elemento da posição 0 da lista
print('Depois do pop2:   ',lista)                        # Resultado: [1, 3, 12, 8, 2, 7, 10, 11]


# O método ".remove()" remove o elemento que for passado como parâmetro
lista.remove(7) #Remove o elemento 7 da lista
print('Depois do remove: ',lista)                        # Resultado: [1, 3, 12, 8, 2, 10, 11]
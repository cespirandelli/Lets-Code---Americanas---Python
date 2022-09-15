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
lista.pop(0) #Remove o elemento da posição 0 da list (indice 0, elemento 20)
print('Depois do pop2:   ',lista)                        # Resultado: [1, 3, 12, 8, 2, 7, 10, 11]


# O método ".remove()" remove o elemento que for passado como parâmetro
# Mas nesse é necessário passar o índice do elemento que queremos remover
lista.remove(7) #Remove o elemento 7 da lista, se houver mais de um 7, ele remove o primeiro que encontrar
print('Depois do remove: ',lista)                        # Resultado: [1, 3, 12, 8, 2, 10, 11]
# Se o elemento não existir na lista, ocorrerá um erro
lista.remove(lista[0]) #Remove o elemento da posição 0 da lista (indice 0, elemento 1)
print('Depois do remove2:',lista)

# Outra forma para remover um elemento da lista é o del
# Mas nesse é necessário passar o índice do elemento que queremos remover
del lista[0] #Remove o elemento da posição 0 da lista (indice 0, elemento 3)
print('Depois do del:    ',lista)                        # Resultado: [12, 8, 2, 10, 11]
# é possível também deletar uma lista inteira com 
# del lista

'''
    O método ".clear()" remove todos os elementos da lista
    lista.clear() #Remove todos os elementos da lista
    print('Depois do clear:  ',lista)                        # Resultado: []
    Para não prejudicar a lista, vou deixar comentado desta forma para ter destaque
'''
print('\n')

# COUNT
# O método ".count()" conta quantas vezes um elemento aparece na lista
lista = [15,1,6,4,8,9,5,1,3,6,8,10,15,7,14,1, 11, 7, 2, 6, 9, 11, 15]
print('Tamano da lista:   ', len(lista))
print("Contagem de 1: ", lista.count(1))
print("Contagem de 2: ",lista.count(2))
print("Contagem de 3: ",lista.count(3))
print("Contagem de 4: ",lista.count(4))
print("Contagem de 5: ",lista.count(5))
print("Contagem de 6: ",lista.count(6))
print("Contagem de 7: ",lista.count(7))

# INDEX
# O método ".index()" retorna o índice do elemento passado como parâmetro
print("Índice do elemento 9:  ", lista.index(9))
print("Índice do elemento 2:  ", lista.index(2))
print("Índice do elemento 15: ", lista.index(15), '-> Lembrando que o índice começa em 0')

# SORT
# O método ".sort()" ordena a lista em ordem crescente ou decrescente
lista.sort() #Ordena a lista em ordem crescente
print('Depois do sort:     ',lista)
lista.sort(reverse=True) #Ordena a lista em ordem decrescente
print('Depois do sort2:    ',lista)


# FUNÇÕES PARA LISTAS
# len() -> Retorna o tamanho da lista
print('Tamanho da lista: ', len(lista))

# max() -> Retorna o maior elemento da lista
print('Maior elemento:   ', max(lista))
# min() -> Retorna o menor elemento da lista
print('Menor elemento:   ', min(lista))

# sum() -> Retorna a soma de todos os elementos da lista
print('Soma dos elementos:', sum(lista))
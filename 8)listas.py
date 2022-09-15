'''
    Para que servem as listas?                       Para armazenar dados
    
    Como criar uma lista?                            Usando colchetes []
    
    Como adicionar um item a uma lista?              Usando o método append(), insert() ou extend()
    
    Como remover um item de uma lista?               Usando o método remove(), pop() ou del()
    
    Como ordenar uma lista?                          Usando o método sort()
    
    Como inverter uma lista?                         Usando o método reverse()
    
    Como contar quantos itens uma lista possui?      Usando a função len()
    
    Como descobrir o índice de um item de uma lista? Usando o método index()
    
    Como acessar um item de uma lista?               Usando o índice do item entre colchetes []
    
    Como acessar um intervalo de itens de uma lista? Usando o índice do primeiro item e do último item entre colchetes []
    
    Como acessar os últimos itens de uma lista?      Usando o índice -1 e -2 e assim por diante
'''

# Antes desta aula, vimos que podemos armazenar apenas um valor em uma variável
# Por exemplo, podemos armazenar o nome de uma pessoa em uma variável
nome = 'João'

# Mas e se quisermos armazenar mais de um valor? 
# Por exemplo, o nome e a idade de uma pessoa?
# Para isso, podemos utilizar uma lista
# Uma lista é um conjunto de valores, que podem ser de qualquer tipo
lista = ['João', 26, 1.75, True] # Nome do tipo string, idade do tipo inteiro, 
                                 # altura do tipo float e se é maior de idade do tipo booleano
print(lista, type(lista)) # Resultado: ['João', 26, 1.75] <class 'list'>

'''
    Em exemplo de outras aulas, vimos que se quisermos armazenar três notas, temos que criar três variáveis.
    Porém, se quisermos armazenar 100 notas, teremos que criar 100 variáveis. Tornando o código muito verboso.
    Para facilitar esta operação podemos utilizar listas. 

'''

# Antes
nota1 = 10
nota2 = 8
nota3 = 9

# Com lista
notas = [10, 8, 9]

# Podemos também criar uma lista vazia
lista_vazia = []
# Outra forma de criar uma lista vazia
lista_vazia = list() #utilizamos a função list() para converter alguma estrutura em uma lista

# Podemos criar uma lista que possui outras listas dentro dela
lista = ['João', 26, 1.75, True, ['Python', 'Java', 'C#']] # Lista de 5 itens, sendo o último uma lista de 3 itens

# Podemos também criar uma lista com valores repetidos
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]



# Indexação e slices

lista = [10, 'Walisson', 3.1415, True] 
# Podemos acessar cada item da lista utilizando o índice do item
# O índice de um item é a sua posição na lista
# O primeiro item da lista possui o índice 0
# O segundo item da lista possui o índice 1
# O terceiro item da lista possui o índice 2
# E assim por diante
# Podemos acessar cada item da lista utilizando o índice do item entre colchetes []
print(lista[0])     # Resultado: 10
print(lista[1])     # Resultado: Walisson
print(lista[2])     # Resultado: 3.1415
print(lista[3])     # Resultado: True
#print(lista[4])    # Resultado: IndexError: list index out of range, não existe o índice 4
print(lista[-1])    # Resultado: True

print(lista[:])     # Resultado: [10, 'Walisson', 3.1415, True]
print(lista[1:])    # Resultado: ['Walisson', 3.1415, True]
print(lista[1:3])   # Resultado: ['Walisson', 3.1415]
print(lista[1:-1])  # Resultado: ['Walisson', 3.1415] 

'''
    Quando realizamos o slice, o último número não é incluído
    
    Ou seja, ao rodar lista[1:3], estamos pegando os itens da posição 1 até a posição 2
    Ou seja, os itens da posição 1 e 2
   
    Quando rodamos lista[1:-1], estamos pegando os itens da posição 1 até a penúltima posição
    Ou seja, os itens da posição 1 e 2
'''

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(lista[1:10:2])    # Resultado: [20, 40, 60, 80, 100]
print(lista[1::2])      # Resultado: [20, 40, 60, 80, 100]
# O terceiro número é o passo, ou seja, a cada quantos itens ele pula
# Neste exemplo, ele pula de 2 em 2
# Funciona como o range(x,y,z) que vimos anteriormente, onde o z é o passo
print(lista[::2])       # Resultado: [10, 30, 50, 70, 90]

# Agora iremos percorrer todos os elementos da lista utilizando o for loop

for elemento in lista:
    print(elemento)


# Outra forma que podemos percorrer os elementos da lista, será utilizando o tamanho da lista e seus índices

print('Comprimento da lista: ', len(lista)) #len sempre tras a quantidade de elementos que existem dentro 
                                            #de alguma estrutura de dados.

for i in range(len(lista)):
    print(i)            #Resultado: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
'''
# Note que no segundo for loop, que estamos utilizando o range(len(lista))
# O range irá gerar uma lista de números de 0 até 9, que é o tamanho da lista
# Ou seja, seus índices
'''

# Podemos então percorrer os elementos da lista utilizando o índice e o tamanho da lista

for i in range(len(lista)):
    print(lista[i])     # Resultado: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
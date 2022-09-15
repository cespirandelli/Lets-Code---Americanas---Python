'''
    Para que servem as listas?                       Para armazenar dados
    
    Como criar uma lista?                            Usando colchetes []
    
    Como adicionar um item a uma lista?              Usando o método append() ou insert()
    
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
lista = ['João', 26, 1.75] # Nome do tipo string, idade do tipo inteiro e altura do tipo float
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
lista_vazia = list()
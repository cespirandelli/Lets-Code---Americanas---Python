# O que são dicionários ? 
'''
    Dicionários são coleções de dados que são armazenados em pares de chave e valor.
    Dicionários são mutáveis, ou seja, podemos alterar seus valores.
    Dicionários são delimitados por chaves {}.
    Dicionários são indexados por chaves, e não por índices.
    Dicionários são heterogêneos, ou seja, podemos armazenar diferentes tipos de dados.
    Dicionários são iteráveis, ou seja, podemos percorrer seus valores.
    Dicionários são ordenados, ou seja, seus valores são armazenados em ordem.
    Dicionários são dinâmicos, ou seja, podemos adicionar e remover valores.
    Dicionários são únicos, ou seja, não podem ter chaves repetidas.
    Dicionários são case sensitive, ou seja, diferenciam letras maiúsculas de minúsculas.

'''

# Criando um dicionário
dicionario = {'nome': 'João', 'idade': 25, 'altura': 1.75} #chaves: nome, idade, altura
                                                           #valores: João, 25, 1.75
'''
Exemplificando:
    Quando usávamos lista, se quisermos saber a idade, seria na seguinte lógica:
    lista[1] #pois iria buscar o elemento 2, ou seja, a idade dentro da lista.
    mas em dicionários:
    dicionario['idade'] #não usamos índices
'''

dicionario_vazio = {}
dicionario_por_funcao = dict()

# ao invés de usar índices, usamos chaves para acessar os valores
print(dicionario['nome'])                                  # João

# podemos acessar os valores de uma chave usando o método get()
print(dicionario.get('idade'))                             # 25

# podemos alterar os valores de uma chave
dicionario['idade'] = 26
print(dicionario)                                          # {'nome': 'João', 'idade': 26, 'altura': 1.75}

# como adicionar chave e valor em um dicionário
dicionario['peso'] = 80
dicionario['programador'] = 'Ainda não'
print(dicionario)                                          # {'nome': 'João', 'idade': 26, 'altura': 1.75, 'peso': 80}

# podemos remover uma chave e seu valor
del dicionario['peso']
print(dicionario)                                          # {'nome': 'João', 'idade': 26, 'altura': 1.75}

# podemos percorrer um dicionário usando o laço for
for chave in dicionario:
    print(chave, dicionario[chave])                        # com essa estrutura, percorremos tanto as chaves e seus valores

'''
    O método items()        retorna uma lista de tuplas, onde cada tupla é composta por uma chave e seu valor.
    o método values()       retorna os valores do dicionário
    o método keys()         retorna as chaves do dicionário
    o método clear()        limpa o dicionário
    o método copy()         copia o dicionário
    o método pop()          remove um item do dicionário
    o método popitem()      remove o último item do dicionário
    o método update()       atualiza o dicionário
    o método fromkeys()     cria um dicionário com as chaves e valores passados como parâmetro
    o método setdefault()   retorna o valor de uma chave, se a chave não existir, cria a chave com o valor passado como parâmetro
    o método len()          retorna o tamanho do dicionário
    o método sorted()       retorna uma lista com as chaves do dicionário ordenadas
'''

# Como saber se uma chave já existe no dicionário?
print(dicionario.keys())
print('peso' in dicionario)
print('altura' in dicionario)

# Como saberos itens que existem no dicionário?
print(dicionario.items())

# Como saber os valores já existentes no dicionário?
print(dicionario.values())
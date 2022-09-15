# O que são funções? 
# Algo que é criado para ser utilizado repetidas vezes.

'''
    Quero saber quantos elementos tenho dentro de uma lista. Posso usar um for loop ou while loop? 
    Sim, mas é mais fácil usar a função len(), pois ela já existe e é mais fácil de usar.
'''

'''
# Funções já utilizadas anteriormente:
print()        # Imprime algo na tela
input()        # Pega uma entrada do usuário
len()          # Retorna o tamanho de algo
type()         # Retorna o tipo de algo
max()          # Retorna o maior valor de algo
'''

            # # Função inicial
            # def funcao(a):
            #     print('Olá, sou uma função', a)

            # # Chamando a função
            # funcao('teste')

# Função inicial (com parâmetros)

def saudacao(nome):
    print(f'\nOlá! Seja muito bem vindo(a) {nome} aqui você irá aprender a programar!!') 
    # utilizar f-string fica mais polido, do que separação de virgula.
    print('É um prazer tê-lo por aqui, espero que se dedique no curso (:\n')

saudacao('César')       # funções podem ser chamadas para executar um bloco de código de forma simples
saudacao('Beatriz')     # como esta função recebe o parâmetro "nome", é necessário escrever uma sting quando
saudacao('Judite')      # a função é chamada, mas podemos criar funções sem parâmetros

# Funcão sem parâmetros

def saudacao2():
    print('Salve salve, seja muito bem vindo ao curso de Python!')
    print('Este é um exemplo de função que não recebe parâmetros\n')

saudacao2()


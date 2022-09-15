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


# Funcão inicial (sem parâmetros)

def saudacao2():
    print('Salve salve, seja muito bem vindo ao curso de Python!')
    print('Este é um exemplo de função que não recebe parâmetros\n')

saudacao2()

# Função inicial (com parâmetros)

def saudacao(nome, curso):
    print(f'\nOlá! Seja muito bem vindo(a) {nome} aqui você irá aprender a programar!') 
    # utilizar f-string fica mais polido, do que separação de virgula.
    print(f"É um prazer tê-lo(a) por aqui, espero que se dedique no curso de {curso} (: \n")
    print('\n')

saudacao('César', 'Python')         # funções podem ser chamadas para executar um bloco de código de forma simples
saudacao('Beatriz', 'SQL')          # como esta função recebe o parâmetro "nome", é necessário escrever uma sting quando
saudacao('Judite', 'PowerBI')       # a função é chamada, mas podemos criar funções sem parâmetros



# Funçõescom parâmetros default

def saudacao(nome, curso='Python'): # definimos que Python será escolhido por padrão 
                                    # caso não haja nenhum outro input dentro da chamada da função
    print(f'\nOlá! Seja muito bem vindo(a) {nome} aqui você irá aprender a programar!') 
    print(f"É um prazer tê-lo(a) por aqui, espero que se dedique no curso de {curso} (: \n")

saudacao('César')               # Não é necessário colocar outra entrada, caso queira a resposta padrão.
saudacao('Beatriz', 'SQL')      # Neste caso, como foi utilizado a segunda entrada, altera-se dentro da função.
saudacao('Judite', 'PowerBI')   

# Funções com retorno
'''
    Geralmente não é comum uma função imprimir algo na tela, mas sim retornar um valor.
    Desta forma podemos utilizar o retorno da função para fazer outras coisas.

'''
def soma(num1=0, num2=0):
    return num1 + num2      # Depois de utilizar o return, a função é encerrada.
                            # Não é possível utilizar o print() ou qualquer outra ação após o return.
                            
resultado = soma(5, 7) #podemos atribuir o retorno da função a uma variável

print(f'O resultado da soma é {resultado}.') # e/ou podemos imprimir o retorno da função num segundo momento

'''
    Agora vamos realizar uma função juntando tudo que já vimos anteriormente.
'''

def calculadora(num1=0, num2=0, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '//':
        return num1 // num2
    elif operacao == '**' or '^':
        return num1 ** num2

resultado1 = calculadora(10,20,'-')
resultado2 = calculadora(10,20,'//') 
print(resultado1, resultado2)
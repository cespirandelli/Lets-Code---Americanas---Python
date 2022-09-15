# Iremos estudar o laço de repetição for
# O for é um laço de repetição que executa uma ação
# Criamos esta repetição de forma controlada, ou seja,
# sabemos quantas vezes será necessário repetir aquela ação

for variavel in range(1, 6):  # range(0,10) é um objeto(função) que gera uma sequência de números
                               # de 0 a 9, ou seja, 10 números.
                               # O for irá repetir a ação 10 vezes, uma para cada número
                               # gerado pelo objeto range(0,10), 10 é o limite superior, não incluso
                               # Se eu quiser que o for repita 5 vezes, eu posso usar
                               # range(0,5) ou range(5), neste caso o 5 não será incluído
                               # Quando uso range(1,6), inicio em 1 e vou até 5, o 6 não é incluído
    print(variavel)

print('\n')

'''
    A função range() pode receber 3 parâmetros, o primeiro é o valor inicial
    o segundo é o valor final e o terceiro é o passo, ou seja, a cada iteração
    o valor da variável será incrementado de acordo com o passo informado
    
    range(0,10,2) irá gerar uma sequência de números de 0 a 9, pulando de 2 em 2
    0, 2, 4, 6, 8
    range(0,10,3) irá gerar uma sequência de números de 0 a 9, pulando de 3 em 3
    0, 3, 6, 9
    range(0,10,4) irá gerar uma sequência de números de 0 a 9, pulando de 4 em 4
    0, 4, 8
    range(0,10,5) irá gerar uma sequência de números de 0 a 9, pulando de 5 em 5
    0, 5
'''

for variavel in range(0, 11, 2): 
    print(variavel)

# Quando o for será útil?
# Quando sabemos quantas vezes será necessário repetir uma ação

'''
    Exemplo: quero pegar 3 notas de um aluno e calcular a média
'''
soma = 0

for i in range(1,4):
    nota = float(input(f'Informe a nota {i}: ')) # quando utilizamos o f-string, podemos colocar uma variavel dentro da string
                                                 # usando chaves, neste caso, chamando a variável i
    soma += nota       #isto é uma variável acumuladora
                        # a cada iteração, o valor da variável media será incrementado
                        # com o valor da variável nota

print('Média: ', round(soma/3, 2)) # round() arredonda o valor para 2 casas decimais, se eu quiser 3 casas decimais, uso round(soma/3, 3)
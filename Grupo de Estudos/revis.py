# o que é uma variavel
# espaço de memoria 
# tipos de variaiveis
# inteiros, quebrados, texto, boleano
# int   -   float   -   str  - True or False
#  7    -    7.0    -   '7'  -  7 == 7 = True
#                               7 == '7' = False
#num = int(input('Digite qualquer coisa: '))
# print(type(num))   
# estruturas basicas 
# operadores aritmeticos 
#  + - / // % * **
#  5 / 2 == 2.5
#  5 // 2 == 2
#  5 % 2 == 1
# =  ==  != 
# if, elif e else
# estrutura de seleção
# se algo for menor que algo então
# deve acontecer alguma coisa
# if num < 10:
#     print("Numero menor que 10")
# elif num == 10:
#     print("Numero igual a 10")
# else:
#     print("Numero maior que 10")
# while 
# contador = 1
# # enquanto o contador for menor que 10
# #       2      < 10
# while contador <= 10:
#     # me mostre o valor de contador
#     #        2
#     print(contador)
#     # e acreste um ao contador
#     # 2      =   2      + 1
#     contador = contador + 1
# função
#   nome  argumentos
# def hello(meu_nome):
#     #return
#     print('Olá', meu_nome)
# # chamada da função
# nome = input("Informe seu nome: ")
# hello(nome)

def num_par(num):
    if num % 2 == 0:
        print("O numero {} par ".format(num))
    else:
        print("O numero {} é impar ".format(num))

# for

# listas 

# crie um programa que faz a soma de 2 numeros
# tipos primitivos em python
# n1 é uma variavel, ela esta guardando o valor que o usuario deu como entrada 
n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
soma = n1 + n2
print('A soma é ', soma)
# A solução apresentada anteriormente esta errada, pois seu resultado sera a junção de 2 strings, o que não representa o resultado real busdado pelo programa
# Aqui podemos ver que usamos a atribuição do tipo primitivo 'int' para converter o valor informado pelo usuario em um valor inteiro
num_1 = int(input('Informe o primeiro valor: '))
num_2 = int(input('Informe o segundo valor: '))
soma_real = num_1 + num_2
print('A soma entre {} e {} vale {}'.format(num_1, num_2, soma_real))

# Entenda que na forma 1, o que estava acontecendo era uma concatenação e não usa soma. Concatenação é o ato de 'juntar/somar' duas ou mais strings
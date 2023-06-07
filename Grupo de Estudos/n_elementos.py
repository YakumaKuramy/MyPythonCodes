# 2- Faça um programa que leia N elementos de um vetor e um valor de código. Se o código
# for 1, mostrar o vetor na ordem direta, se o código for 2, mostrar o vetor na ordem inversa.

N = [0,1,2,3,4,5,6,7,8,9]
cod = int(input("Informe um valor: "))
index = len(N)
count = 0

while count < index:
    if cod == 1:
        print(N[count])
    elif cod == 2:
        print(N[count])
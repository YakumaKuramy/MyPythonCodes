"""Dado um numero não-negativo n, determinar n! = n fatorial
exemplo = 5! = 5*4*3*2*1 = 120
"""

n = int(input("Informe um valor: "))
#forma feita decrementando 

count = n - 1
prod = n
while count > 1:
    prod = prod * count 
    count -= 1
print("{} ! = {}".format(n,prod))

#forma acrecentando 
count = 2
prod = 1
while count <= n:
    prod = prod * count 
    count += 1
print("{} ! = {}".format(n,prod))
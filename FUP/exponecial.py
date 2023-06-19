base = int(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente: "))

count = 0
produto = 1

while count < expoente:
    produto = produto * base
    count += 1
print("{} elevado a {} é igual a {}".format(base,expoente,produto))
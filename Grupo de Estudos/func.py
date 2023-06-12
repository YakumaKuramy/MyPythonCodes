def num_par(num):
    if num % 2 == 0:
        print("O numero {} par ".format(num))
    else:
        print("O numero {} é impar ".format(num))

num = int(input("Informe um numero "))

num_par(num)


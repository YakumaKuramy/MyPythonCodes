# Implemente um programa que recebe a temperatura em graus Celsius e converte para Fahrenheit. 
c = float(input("Informe a temperatura em Celcius: "))
f = ((c / 5) * 9 ) + 32
print("A temperatura é {} que equivale a {}".format(c, f))
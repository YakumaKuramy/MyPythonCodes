#pequeno teste de mudança de cores em python
#nessa primeira parte do codigo eu testo os formatos usando os modulos de cores
name = input("Your name: ")
print("\033[31m{}\033[0m".format(name))
print("\033[35m{}\033[0m".format(name))

#nesse segundo importo uma biblioteca
from colorama import Fore, Style

print(Fore.RED + "Texto em vermelho = {}".format(name))
print(Fore.GREEN + "Texto em verde = {}".format(name))
print(Style.RESET_ALL + "Texto normal = {}".format(name))

# a segunda forma me parece melhor, dessa forma vou fazer mais alguns testes para validação de uso

#nesse caso, a primeira função vai tratar as entradas da função como texto, dessa forma para usar elas é preciso fazer a converção do tipo int para str

print("---> Soma de texto <---")


def color_text(a, b):
  print(Fore.RED + a)
  print(Fore.GREEN + b)
  return Fore.BLUE + (a + b)


a = input("Digite algo: ")
b = input("Digite algo: ")

print(color_text(a, b))
#perceba que foi preciso resetar os estilos
print(Style.RESET_ALL)

print("---> Soma de inteiros <---")
#agora faremos a converção para que ela imprima o resultado da soma e não junte os 2 textos como foi feito anteriormente


def color_int_soma(a, b):
  print(Fore.RED + str(a))
  print(Fore.GREEN + str(b))
  return Fore.BLUE + str((a + b))


a = int(input("Digite algo: "))
b = int(input("Digite algo: "))

print(color_int_soma(a, b))

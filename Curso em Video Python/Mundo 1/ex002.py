# perceba que toda saida desse programa sera do tipo str, pois não há conversão em momento algum para nenhum outro tipo
# perceba que o objeto 'a' tem muitos metodos que permitem a verificação, o que pode e sera usado para otmizar os processos, simplificando conforme necessario
a = input('Digite algo: ')
print('O tipo primitivo dessa variavel é {}'.format(type(a)))
print('So tem espaços? {}'.format(a.isspace()))
print('É um numero? {}'.format(a.isnumeric()))
print('É alfabetico? {}'.format(a.isalpha()))
print('É alfanumeiro? {}'.format(a.isalnum()))
print('Esta apenas em maiusculas? {}'.format(a.isupper()))
print('Esta apenas em minusculas? {}'.format(a.islower()))
print('Esta capitalizada? {}'.format(a.istitle()))
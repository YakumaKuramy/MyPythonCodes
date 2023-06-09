# neste exemplo usaremos operadores aritmeticos 
# perceba o uso da '\n' para quebrar a linha dentro do print e o uso do 'end=' '' para continuar a impressão da linha seguinte junto da anterior
n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} \n e a divisão é {:.3f}'.format(s,m,d), end=' -> ')
print('A divisão inteira é {} e a potencia {}'.format(di, e))
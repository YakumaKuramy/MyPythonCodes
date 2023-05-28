#importamos a biblioteca completa, não esta errado, mas consome mais memoria 
import random
# uma outra forma de fazer isso é importanto uma parte especifica da biblioteca 
ale_0 = random.randint(0,9)
print(ale_0)
#aqui importamos apenas o 'randint' da biblioteca random
from random import randint
#e o codigo segue igualmente
ale_1 = randint(0,9)
print(ale_1)
# uma outra forma de fazer isso e tornar mais simples é dando nome a parte que vc chamou 
# por exemplo
from random import randint as rd
ale_2 = rd(0,9)
print(ale_2)
#perceba que teremos resultados igual nas saidas mas o codigo é processado de forma diferente
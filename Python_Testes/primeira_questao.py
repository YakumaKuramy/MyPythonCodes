#PRIMEIRO EXERCÍCIO

#bibli da tabela verdade e circuitos lógicos
import ttg
import schemdraw
import schemdraw.logic as logic

#apresentação
print('''
Algebra de Boole
F = ~xyz + xz + x~yz + x~z + xy

Forma Simplificada
F = z + x
''')

print('TABELA-VERDADE E CIRCUITO')
print(ttg.Truths(['z', 'x'], ['z or x']))
with schemdraw.Drawing() as view:
    view.config(unit=.3)
    and_gt = view.add(logic.Or().at((0, 0)).label('F', 'right'))
    view.add(logic.Line().at(and_gt.in1).left(view.unit).label('z', 'left'))
    view.add(logic.Line().at(and_gt.in2).left(view.unit).label('x', 'left'))
view.draw()

from schemdraw.parsing import logicparse
d = logicparse('not ((w and x) or (y and z))', outlabel='$\overline{Q}$')
d.draw()
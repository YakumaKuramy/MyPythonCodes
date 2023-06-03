import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic

d = schemdraw.Drawing()

# Cria os dois componentes "AND"
and1 = logic.And()
and2 = logic.And()

# Adiciona os componentes ao circuito
input_a = d.add(and1.in1)
input_b = d.add(and1.in2)
output = d.add(and2.out)

# Conecta as saídas e as entradas dos componentes
d.add(elm.Line().right().at(and1.out))
d.add(elm.Line().right().at(input_a.start))
d.add(elm.Line().right().at(input_b.start))
d.add(elm.Line().left().at(and2.in1))
d.add(elm.Line().left().at(and2.in2))

d.draw()

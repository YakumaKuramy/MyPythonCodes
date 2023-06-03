import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic

d = schemdraw.Drawing()

# Cria os dois componentes "AND" com no máximo 2 entradas cada
and1 = logic.And(inputs=2)
and2 = logic.And(inputs=2)

# Adiciona os componentes ao circuito
input_a1 = d.add(elm.Dot())
input_b1 = d.add(elm.Dot())
output1 = d.add(and1)

input_a2 = d.add(elm.Dot())
#input_b2 = d.add(elm.Dot())
output2 = d.add(and2)

# Conecta as saídas e as entradas dos componentes
d.add(elm.Line().right().at(input_a1.end).to(output1.in1))
d.add(elm.Line().right().at(input_b1.end).to(output1.in2))

d.add(elm.Line().right().at(input_a2.end).to(output2.in1))
#d.add(elm.Line().right().at(input_b2.end).to(output2.in2))

d.draw()

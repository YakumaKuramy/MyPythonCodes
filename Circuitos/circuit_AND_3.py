#Circuito simples com 3 ou mais entradas não definidar objetivamente
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic

d = schemdraw.Drawing()

and_gate = logic.And(inputs=4)

d.add(and_gate)
d.draw()
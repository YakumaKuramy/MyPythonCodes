#Circuito simples com duas entradas não definidar objetivamente
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic

d = schemdraw.Drawing()

and_gate1 = logic.And()
and_gate2 = logic.And()

d.add(and_gate1)
d.add(and_gate2)

d.draw()
#Circuito simples com duas entradas não definidar objetivamente
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic


d = schemdraw.Drawing()

and_gate = logic.And()

d.add(and_gate)
d.draw()
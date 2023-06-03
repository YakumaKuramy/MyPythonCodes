import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic

d = schemdraw.Drawing()

# Cria as entradas do circuito
input_a = d.add(elm.Dot()).label('A')
input_b = d.add(elm.Dot()).label('B')

# Cria a porta lógica "AND" e a conecta às entradas
and_gate = logic.And()
output = d.add(and_gate)

# Conecta as entradas à porta lógica
d.add(elm.Line().right().at(input_a.end))
d.add(elm.Line().right().at(input_b.end))

# Conecta a saída da porta lógica à próxima parte do circuito
d.add(elm.Line().right().at(output.out))

# Dá um nome à saída do circuito
output.label('Out')

d.draw()

import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic

d = schemdraw.Drawing()

# Cria as entradas do circuito e adiciona os nomes
input_a = d.add(elm.Dot())
d.add(elm.Text('A', anchor='w').at(input_a.start))
input_b = d.add(elm.Dot())
d.add(elm.Text('B', anchor='w').at(input_b.start))

# Cria a porta lógica "AND" e a conecta às entradas
and_gate = logic.And()
output = d.add(and_gate)

# Conecta as entradas à porta lógica
d.add(elm.Line().right().at(input_a.end))
d.add(elm.Line().right().at(input_b.end))

# Conecta a saída da porta lógica à próxima parte do circuito
d.add(elm.Line().right().at(output.out))

# Adiciona o nome à saída do circuito
d.add(elm.Text('Out', anchor='e').at(output.out))

d.draw()

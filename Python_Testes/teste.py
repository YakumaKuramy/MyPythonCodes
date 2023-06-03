import ttg
import schemdraw
import schemdraw.logic as logic

with schemdraw.Drawing() as view:
    view.config(unit=.3)

view.draw()
from schemdraw.parsing import logicparse
d = logicparse('not ((w and x) or (y and z))', outlabel='$\overline{Q}$')
d.draw()
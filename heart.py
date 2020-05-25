from simulation import System, loops
from renderer import Render
from math import pi

test = System()
test.add_point(350, 600)
test.add_point(350, 600-170/2)
test.add_point(350, 600-585/2)
test.add_base(0, 215.1/2, 0, -pi)
test.add_line(0, 1, 389.1/2)
test.add_line(1, 2, 856.4/2)
test.add_draw(2)
test.main_loop(end=loops(5000), render=Render([700, 800], {"Line":'black', "Point":'CadetBlue1', "Drive":'maroon', "Drawer":"red"}))
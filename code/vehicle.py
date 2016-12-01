# Vehicle class
# Created by: Hamza Salman
# Created for: TEJ3M1

from vehicle import *

car1 = Vehicle()
car2 = Vehicle()

car1 = Vehicle('blue', 'B263', 2, 300)
car1.vehicle_info()
car1.accelerate(235)
car1.current_state()

car2.vehicle_info()
car2.accelerate(285)
car2.brake(35)
car2.current_state()

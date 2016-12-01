# Vehicle class
# Created by: Hamza Salman
# Created for: TEJ3M1

class Vehicle:
	
	_speed = 0
	_gear = 0
	_colour = ''
	_liscense_plate = ''
	_number_of_doors = 0
	_maximum_speed = 0
	
	def __init__(self, colour, liscence_plate, number_of_doors, maximum_speed):
		
		self._colour = colour
		self._liscense_plate = liscence_plate
		self._number_of_doors = number_of_doors
		self._maximum_speed = maximum_speed
		
	
	def accelerate(self, speed_increase):
		print 'accelerating by ' + str(speed_increase) + 'km/h'
		self._speed = self._speed + speed_increase
		if self._speed > self._maximum_speed:
			self._speed = self._maximum_speed
		self.gear()
			
	def brake(self, speed_decrease):
		print 'braking by ' + str(speed_decrease)
		self._speed = self._speed - speed_decrease
		if self._speed < 0:
			self._speed = 0
		self.gear()
		
	def gear(self):
		if self._speed < self._maximum_speed/6:
			self._gear = 1
		elif self._speed < (self._maximum_speed/6*2):
			self._gear = 2
		elif self._speed < (self._maximum_speed/6*3):
			self._gear = 3
		elif self._speed < (self._maximum_speed/6*4):
			self._gear = 4
		elif self._speed < (self._maximum_speed/6*5):
			self._gear = 5
		else:
			self._gear = 6
		
	def vehicle_info(self):
		print 'Colour: ' + self._colour
		print 'Liscense plate: ' + self._liscense_plate
		print 'Number of doors: ' + str(self._number_of_doors)
		print 'Maximum speed: ' + str(self._maximum_speed) + 'km/h'
		
	def current_state(self):
		print 'Current Speed: ' + str(self._speed) + 'km/h'
		print 'Current Gear: ' + str(self._gear) + '\n'
		
myCar = Vehicle('blue', 'B263', 2, 300)
myCar.vehicle_info()
myCar.accelerate(235)
myCar.current_state()

myCar.vehicle_info()
myCar.accelerate(285)
myCar.brake(35)
myCar.current_state()

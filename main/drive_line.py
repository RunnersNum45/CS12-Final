from math import sin, cos
from point import Point
from math import pi

class Drive_line:
	def __init__(self, parent, length, inital_rotation, speed):
		self.parent = parent #Point
		self.length = length
		self.speed = speed

		self.rotation = inital_rotation

	def drive(self, dt):
		self.rotation += self.speed*dt

	@property
	def end_point(self, prev={}):
		if (self.rotation, self.parent.pos) in prev.keys():
			return prev[(self.rotation, self.parent.pos)]
		else:
			prev.clear()
			prev[(self.rotation, self.parent.pos)] = Point(self.length*cos(self.rotation), self.length*sin(self.rotation))+self.parent
			return prev[(self.rotation, self.parent.pos)]

	@property
	def x(self):
		return self.end_point.x

	@property
	def y(self):
		return self.end_point.y

	@property
	def pos(self):
		return self.end_point.pos

	def __str__(self):
		return str(self.end_point)
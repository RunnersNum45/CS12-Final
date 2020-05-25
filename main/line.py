from math import atan2
from point import Point
from drive_line import Drive_line

class Line(Drive_line):
	def __init__(self, parent, intersect, length):
		self.parent = parent #Drive_line or Line

		self.intersect = intersect
		self.length = length

	@property
	def rotation(self):
		return atan2(self.intersect.y-self.parent.y, self.intersect.x-self.parent.x)

	def drive(self):
		raise ("Line class does not have method drive()")
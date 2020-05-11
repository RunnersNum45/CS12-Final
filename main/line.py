from math import *
import numpy as np

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@property
	def pos(self):
		return (self.x, self.y)

	def __str__(self):
		return "(x:{}, y:{})".format(self.x, self.y)


class Drive_line:
	def __init__(self, parent, length, inital_rotation):
		self.parent = parent #Point
		self.length = length

		self.rotation = inital_rotation
		self.children = []

	@property
	def end_point(self):
		return Point(self.length*cos(self.rotation)+self.parent.x, self.length*sin(self.rotation)+self.parent.y)

	@property
	def x(self):
		return self.end_point.x

	@property
	def y(self):
		return self.end_point.y

	def drive(self):
		self.rotation += pi/10
		return self.children


class Line:
	def __init__(self, parent, intersect, length):
		self.parent = parent #Drive_line or Line
		parent.children.append(self)

		self.intersect = intersect
		self.length = length

	@property
	def rotation(self):
		return atan2(self.intersect.y-self.parent.y, self.intersect.x-self.parent.x)

	@property
	def end_point(self):
		return Point(self.length*cos(self.rotation)+self.parent.x, self.length*sin(self.rotation)+self.parent.y)

	@property
	def x(self):
		return self.end_point.x

	@property
	def y(self):
		return self.end_point.y

if __name__ == '__main__':
	points = [Point(0, 0), Point(15, 0)]
	main = Drive_line(points[0], 10, 0)
	second = Line(main, points[1], 20)

	for x in range(10):
		print(main.end_point, second.end_point)
		main.drive()
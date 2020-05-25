from line import Line
from point import Point
from drive_line import Drive_line
from math import pi
from renderer import Render
from time import sleep, time
from drawer import Drawer

def print_out(sys):
	print(" ".join(str(line) for line in sys.lines))

def loops(n):
	def looper(sys, rec=[0]):
		if rec[0] < n:
			rec[0] += 1
			return False
		else:
			return True
	return looper


class System:
	def __init__(self):
		self.points = []
		self.lines = []
		self.drive_lines = []
		self.drawers = []

	def add_point(self, x, y):
		self.points.append(Point(x, y))
		return self.points

	def add_base(self, parent, length, inital_rotation, speed):
		self.drive_lines.append(len(self.lines))
		self.lines.append(Drive_line(self.points[parent], length, inital_rotation, speed))

	def add_line(self, parent, intersect, length):
		self.lines.append(Line(self.lines[parent], self.points[intersect], length))

	def add_draw(self, parent):
		self.drawers.append(Drawer(self.lines[parent]))

	def main_loop(self, render=None, end=None):
		if end == None:
			end = lambda sys: False
		if render == None:
			render = lambda sys: print_out(sys)

		drive_lines = [self.lines[x] for x in self.drive_lines]

		start = time()
		while not end(self):
			dt = time()-start
			start = time()
			for base in drive_lines:
				base.drive(dt)
			render(self)
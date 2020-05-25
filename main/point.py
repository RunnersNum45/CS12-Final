class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@property
	def pos(self):
		return (self.x, self.y)

	def __str__(self):
		return "(x:{}, y:{})".format(self.x, self.y)

	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y)

	def __neg__(self):
		return Point(-self.x, -self.y)

	def __sub__(self, other):
		return self+(-other)
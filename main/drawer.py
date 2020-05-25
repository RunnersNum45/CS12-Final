class Drawer:
	def __init__(self, parent):
		self.parent = parent

	def __getattr__(self, attr):
		return getattr(self.parent, attr)
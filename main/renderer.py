from tkinter import *

def create_circle(canvas, x, y, r, **kwargs):
	return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

class Render:
	def __init__(self, dims, colors={"Line":'black', "Point":'CadetBlue1', "Drive":'maroon', "Drawer":"red"}):
		self.colors = colors

		self.window = Tk()
		self.window.title(id(self))

		self.canvas = Canvas(self.window, width=dims[0], height=dims[1], bg="white")
		self.canvas.pack()
		self.canvas.update()

	def draw(self, sim):
		self.canvas.delete("line")
		self.canvas.delete("drive")

		if len(self.canvas.find_withtag("point")) == 0:
			for point in sim.points:
				create_circle(self.canvas, point.x, point.y, 3, fill=self.colors["Point"], tags="point")

		for i, line in enumerate(sim.lines):
			if i in sim.drive_lines:
				self.canvas.create_line(line.parent.x, line.parent.y, line.end_point.x, line.end_point.y, width=4, fill=self.colors["Drive"], tags="drive")
			else:
				self.canvas.create_line(line.parent.x, line.parent.y, line.end_point.x, line.end_point.y, width=4, fill=self.colors["Line"], tags="line")

		for d in sim.drawers:
			create_circle(self.canvas, d.x, d.y, 3, fill=self.colors["Drawer"], tags="drawer", outline=self.colors["Drawer"])

		self.canvas.update()

	def __call__(self, sim):
		self.draw(sim)

class bounding_box:
	x = 0
	y = 0
	width = 0
	height = 0
	z = 0
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

	def omkrets(self):
		return 0

	def overlaps(self, other_box):

		return False

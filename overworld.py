ENTITY = "E"
OBSTACLE = "O"

class Overworld:
	def __init__(self, x_dim, y_dim):
		self.x_dim = x_dim
		self.y_dim = y_dim
		self.map_list = [[None for x in range(x_dim)] for y in range(y_dim)]
	def get_cell(self, x, y):
		if (x < 0 or x >= x_dim or y < 0 or y >= y_dim):
			return "ERROR"
		else:
			return self.map_list[y][x]
	def add_overworldentity(self, overworldentity):
		self.map_list[overworldentity.y][overworldentity.x] = overworldentity
	def move_overworldentity(self, overworldentity, new_x, new_y):
		
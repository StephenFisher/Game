from debug import *
from overworld import *

import random

dbflag = True

# directions
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

class OverworldEntity:
	def __init__(self, overworld, x, y, debug_name = ""):
		self.datatype = "overworldentity"
		self.x = x # changed by overworld. DO NOT CHANGE IN THIS CLASS
		self.y = y # changed by overworld. DO NOT CHANGE IN THIS CLASS
		self.overworld = overworld
		self.overworld.add_overworldentity(self)
	def get_movement(self):
		pass

class Player(OverworldEntity):
	def __init__(self, overworld, x, y, debug_name = ""):
		super.__init__(self, overworld, x, y, debug_name)
	def get_movement(self):
		pass

class NPC(OverworldEntity):
	def __init__(self, overworld, x, y, debug_name = ""):
		super.__init__(self, overworld, x, y, debug_name)
	def get_movement(self):
		db(dbflag, debug_name + " is moving")
		direction = random.randint(NORTH, WEST)
		while (True):
			if (direction == NORTH):
				if (self.overworld.get_cell(self.x, self.y - 1) == None):
					db(dbflag, debug_name + " is going north")
					self.overworld.move_overworldentity(self, self.x, self.y - 1)
					return
			elif (direction == SOUTH):
				if (self.overworld.get_cell(self.x, self.y + 1) == None):
					db(dbflag, debug_name + " is going south")
					self.overworld.move_overworldentity(self, self.x, self.y + 1)
					return
			elif (direction == EAST):
				if (self.overworld.get_cell(self.x + 1, self.y) == None):
					db(dbflag, debug_name + " is going east")
					self.overworld.move_overworldentity(self, self.x + 1, self.y)
					return
			else:
				if (self.overworld.get_cell(self.x - 1, self.y) == None):
					db(dbflag, debug_name + " is going west")
					self.overworld.move_overworldentity(self, self.x - 1, self.y)
					return
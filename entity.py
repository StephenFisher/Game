from debug import *

dbflag = True

class Entity:
	def __init__(self, name, level, hp, maxhp, attack, defense, speed, exp):
		self.name = name
		self.level = level
		self.hp = hp
		self.maxhp = maxhp
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.exp = exp
	def get_move(self):
		db(dbflag, self.name + " chose move: attack")
		return "attack"
	def give_exp(self, amount):
		db(dbflag, self.name + " gained " + str(amount) + " exp")
		self.exp += amount
		if (int(self.exp / 500) > self.level):
			db(dbflag, self.name + " leveled up from " + str(self.level) + " to " + str(self.level + 1))
			self.level += 1
			self.maxhp += 100
			self.attack += 2
			self.defense += 2
			self.speed += 2
	def write_to(self, filename):
		f = open(filename, 'a')
		f.write("<entity>\n")
		entityline = self.name + ","
		entityline += str(self.level) + ","
		entityline += str(self.hp) + ","
		entityline += str(self.maxhp) + ","
		entityline += str(self.attack) + ","
		entityline += str(self.defense) + ","
		entityline += str(self.speed) + ","
		entityline += str(self.exp) + "\n"
		f.write(entityline)
		f.close()

def parse_entity_line(entityline):
	entitylist = entityline.strip().split(",")
	return Entity(entitylist[0], int(entitylist[1]), int(entitylist[2]), int(entitylist[3]), int(entitylist[4]), int(entitylist[5]), int(entitylist[6]), int(entitylist[7]))
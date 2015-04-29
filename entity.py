from debug.py import *

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
		db(db_flag, self.name + " chose move: attack")
		return "attack"
	def give_exp(self, amount):
		db(db_flag, self.name + " gained " + str(amount) + " exp")
		self.exp += amount
		if (int(self.exp / 500) > self.level):
			db(db_flag, self.name + " leveled up from " + str(self.level) + " to " + str(self.level + 1))
			self.level += 1
			self.maxhp += 100
			self.attack += 2
			self.defense += 2
			self.speed += 2
#Entity: Speed, attack, defence, hp, level

from debug import *

dbflag = True

class Battle:
	def __init__(self):
		pass

	def add_fighters(self, entity1, entity2):
		self.fighter1 = entity1
		self.fighter2 = entity2

	def turn(self):
		move1 = self.fighter1.get_move()
		move2 = self.fighter2.get_move()

		if (move1 == "attack"):
			if (move2 == "attack"):
				if (self.fighter1.speed > self.fighter2.speed):
					#Damage Calculation
					db(dbflag, "Fighter 1 attacks.")
					self.fighter2.hp -= self.fighter1.attack
					db(dbflag, "Fighter 2 HP: " + str(self.fighter2.hp))
					if (self.fighter2.hp <= 0):
						db(dbflag, "Fighter 2 died")
						self.fighter1.give_exp(50)
						return
					else:
						db(dbflag, "Fighter 2 attacks.")
						self.fighter1.hp -= self.fighter2.attack
						db(dbflag, "Fighter 1 HP: " + str(self.fighter1.hp))
						if (self.fighter1.hp <= 0):
							db(dbflag, "Fighter 1 died")
							self.fighter2.give_exp(50)
							return 
				else:
					#Damage Calculation
					db(dbflag, "Fighter 2 attacks.")
					self.fighter1.hp -= self.fighter2.attack
					db(dbflag, "Fighter 1 HP: " + str(self.fighter1.hp))
					if (self.fighter1.hp <= 0):
						self.fighter2.give_exp(50)
						return
					else:
						db(dbflag, "Fighter 1 attacks.")
						self.fighter2.hp -= self.fighter1.attack
						db(dbflag, "Fighter 2 HP: " + str(self.fighter2.hp))
						if (self.fighter2.hp <= 0):
							db(dbflag, "Fighter 2 died.")
							self.fighter1.give_exp(50)
							return

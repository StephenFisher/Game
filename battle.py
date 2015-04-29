#Entity: Speed, attack, defence, hp, level

from debug.py import *

dbflag = True

class Battle:
	def __init__(self):
		pass

	def add_fighters(self, entity1, entity2):
		self.figher1 = entity1
		self.figher2 = entity2

	def turn(self):
		move1 = self.fighter1.get_move()
		move2 = self.fighter2.get_move()

		if (move1 == "attack"):
			if (move2 == "attack"):
				if (fighter1.speed > fighter2.speed):
					#Damage Calculation
					db(dbflag, "Fighter 1 attacks.")
					fighter2.hp -= fighter1.attack
						if (fighter2.hp <= 0):
							fighter1.give_exp(50)
						else:
							fighter1.hp -= fighter2.attack
								if (fighter1.hp <= 0):
									fighter2.give_exp(50) 
				else:
					#Damage Calculation
					fighter1.hp -= fighter2.attack
						if (fighter1.hp <= 0):
							fighter2.give_exp(50)
						else:
							fighter2.hp -= fighter1.attack
								if (fighter2.hp <= 0):
									fighter1.give_exp(50) 

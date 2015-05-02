#Item: Value
#Weapon: Attack
#Armour: Defense

class Item:
	def __init__(self):
		pass

class Weapon(Item):
	def __init__(self):
		super.__init__(self)

class Armour(Item):
	def __init__(self):
		super.__init__(self)

#Subclasses of Weapon
class Magic(Weapon):
	def __init__(self):
		super.__init__(self)

class Archery(Weapon):
	def __init__(self):
		super.__init__(self)

class Melee(Weapon):
	def __init__(self):
		super.__init__(self)

#Subclasses of Armour
class Helmet(Armour):
	def __init__(self):
		super.__init__(self)

class Platebody(Armour):
	def __init__(self):
		super.__init__(self)

class Legs(Armour):
	def __init__(self):
		super.__init__(self)
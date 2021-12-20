class Unit(object):

	def __init__(self, name, country):
		self.name = name
		self.country = country
		self.armor = 400
		self.damage = 50
		self.speed = 80

	def shot(self, enemy):
		enemy.armor = enemy.armor - self.damage
		print(enemy.name, enemy.armor)	
		return "Bah-bah"



	def move(self, enemy):
		
		return "Sir, Yes sir"


tank = Unit('leha', 'sssr')
tank2 = Unit('john', 'usa')

tank.shot(tank2)

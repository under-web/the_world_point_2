
class Unit(object):

	def __init__(self, name, country):
		self.name = name
		self.country = country
		self.armor = 400
		self.damage = 50
		self.speed = 80

	def shot(self, enemy):
		enemy.armor = enemy.armor - self.damage
		print(f'{self.name} наснёс урон {enemy.name} в размере {self.damage} - здоровье {enemy.name} = {enemy.armor}')	
			



	def move(self, enemy):
		
		return "Sir, Yes sir"


tank = Unit('red', 'sssr')
tank2 = Unit('blue', 'usa')

tank.shot(tank2)
print(tank2.armor)

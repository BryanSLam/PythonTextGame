#Base module for monsters

class Monster(object):

	def __init__(self, monsterType):
		self.monsterType = monsterType
		
		#Categorize the different monsters here
		
		#if(monsterType == "name"):
		#self.HP = hit points
		#self.strength = strength bonus
		#self.dexterity = dodge bonus
		#drops = coins, reg monste drops, equips
		
		
		if(monsterType == "slime"):
			self.HP = 12
			self.strength = 2
			self.dexterity = 0
			drops = [10, "jelly"]
			rareDrops = 
		
	
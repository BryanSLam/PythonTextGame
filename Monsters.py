#Base module for monsters
from Items import Item
from random import randint
class Monster(object):

	def __init__(self, monsterType):
		self.monsterType = monsterType
		
		#Categorize the different monsters here
		
		#if(monsterType == "name"):
		#self.HP = hit points
		#self.strength = strength bonus
		#self.dexterity = dodge bonus
		#drops = coins, reg monster drops, equips
		
		#Rare drops have a 20% chance of drop
		#Super rare has 10%
		
		if(monsterType == "Slime"):
			self.HP = 12
			self.strength = 2
			self.dexterity = 0
			self.drops = [randint(5,10), Item("Jelly")]
			self.rareDrops = [Item("Short Sword")]
			self.superRareDrops = [Item("Excalibur")]
		
		elif(monsterType == "Rat-Ta-Ta"):
			self.HP = 10
			self.strength = 3
			self.dexterity = 1
			self.drops =[randint(5,10), Item("Scat")]
			self.rareDrops = [Item("Scat Sword")]
			
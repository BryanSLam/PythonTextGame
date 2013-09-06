#Floor
#Each floor should hold a grid that's dynamically set every time the floor is 
#initialized and a map that is updated whenever a player changes tiles 

#The generatedMap will hold the information the was made when the floor 
#initialized and the user map will contain x's letting the user know where 
#they've already been

#Move set 1-4 = first row 5-8 = second row 9-12 = third row 12-15 = fourth row
from random import randint
from Character import Player

class Floor(object):
#	PROPERTIES
#	generatedMap
#	userMap
#	mounsterCount
#	floorNumber

	def __init__(self, floorNumber, character):
		#Map setup: M for monster, I for item, E for empty
		self.generatedMap = [['E','E','E','E'],['E','E','E','E'],\
		['E','E','E','E'],['E','E','E','E']]
		self.floorNumber = floorNumber
		if(floorNumber == 1):
			self.monsterCount = 2
		
		#monster placement
		
		#Extra comments to explain my thought process
		#The map is 4x4 and the loop runs the number of times needed to fill 
		#the monster count during each iteration of the loop it picks a random 
		#spot on the map and if that spot contains something then handle that
		for i in range (0, self.monsterCount):
			row = randint(0,3)
			column = randint(0,3)
			while(self.generatedMap[row][column] != 'E'):
				row = randint(0,3)
				column = randint(0,3)
			self.generatedMap[row][column] = 'M'
		
		self.displayMap()
			
	def displayMap(self):
		for i in self.generatedMap:
			print "\n"
			print i
		

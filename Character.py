#Character
from random import randint
from Items import Item
class Player():
	def __init__(self, job):
		self.job = job
		self.hitPoints = randint(21,30)
		self.gold = 0
		self.inventory = []
		
		#make stats more job specific later on
		self.strength = randint(5,10)
		self.dexterity = randint(5,10)
		self.intelligence = randint(5,10)
		self.magicPoints = 5 + self.intelligence
		
		#map
		self.userMap = [["[ ]", "[ ]", "[ ]", "[ ]"],\
		["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],\
		["[ ]", "[ ]", "[ ]", "[ ]"]]

	
#Dungeons and dragons mechanics	

#Roll an initial die to see if you can get the attack off then roll for damage
	def attack(self, monsterDexterity, monsterArmor):
		initialRoll = randint(0,20)
		rollToHit = initialRoll + self.dexterity
		critical = false
		if(initialRoll == 20):
			critical = true
		if(rollToHit >= monsterDexterity):
			#If hit commence damage sequence
			if(critical == true):
				return randint(0,6) + randint(0,6) + self.strength -\
				monsterArmor
			else:
				return randint(0,6) + self.strength - monsterArmor
		else:
			print "Missed!"
			return 0
	
#Check the current position if its a valid move, if it is then mark the map
#where the character currently is and update the map where the character has 
#been and return new position	

#The grid is bottom right is 0,0 and top left is 3,3

	#direction is 'n','w','s','e'
	#position is a tuple row, column
	def move(self, direction, position):
		canMove = True
		if(direction == 'w'):
			if(position[1] == 3):
				canMove = False
		elif(direction == 'n'):
			if(position[0] == 3):
				canMove = False
		elif(direction == 's'):
			if(position[0] == 0):
				canMove = False
		elif(direction == 'e'):
			if(position[1] == 0):
				canMove = False	

				
		if(canMove == False):
			return False
	#update the map
		updateMap(position, direction)
	
	#Return new position
		if(direction == 'w'):
			return (position[0],position[1]+1)
		elif(direction == 'n'):
			return (position[0]+1,position[1])
		elif(direction == 's'):
			return (position[0]-1,position[1]+1)
		elif(direction == 'e'):
			return (position[0],position[1]-1)	
		
			
	def newFloor(self):
		self.userMap = [["[O]", "[ ]", "[ ]", "[ ]"],\
		["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],\
		["[ ]", "[ ]", "[ ]", "[ ]"]]

		
	def displayMap(self):
		for i in range(0,4):
			print self.userMap[i]
			print "\n"
			
	def updateMap(self, position, direction):
		self.userMap[position[0]][position[1]] = "[X]"
		if(direction == 'w'):
			return (position[0],position[1]+1)
		elif(direction == 'n'):
			return (position[0]+1,position[1])
		elif(direction == 's'):
			return (position[0]-1,position[1]+1)
		elif(direction == 'e'):
			return (position[0],position[1]-1)	
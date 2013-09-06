#Initial Setup
#The came module will handle all of the event handling as well as acting
#as the overall observer of the other modules
import sys
from random import randint
from Tower import Floor
from Character import Player
from Items import Item

#Helper methods
def displayMenu(character, characterPosition):
	print "What action would you like to take?"
	print "1: Move"
	print "2: Check Map"
	print "3: Item Menu"
	print "0: Quit Game"
	s=-1
	while(s !='1' and s !='2'and s !='3'and s !='0'):
		s = raw_input('>')
		if(s == '1'):
			direction = -1
			while(direction != 'w' and direction != 'e' and direction !='n'\
					and direction != 's'):
				print "Which direction would you like to move in?"
				print "e (east) n (north) s (south) w (west)"
				direction = raw_input('>')
			return character.move(direction, characterPosition)
		elif(s == '0'):
			sys.exit()
			
#Main Menu
menuSelection = 0
while(menuSelection != '1' and menuSelection != '2'):
	print "Press 1 to start a new game or 2 to quit"
	menuSelection = raw_input('> ')

#begin game
if(menuSelection == '1'):
	print """\tYou are inside a tower with 7 floors, each floor containing 
	
	numerous monsters, hidden treasures, and a floor boss at each level.  Only 
	
	by defeating each floor boss will you be allowed to move onto the next floor.

	The rooms are all open space in a 4x4 grid where each turn you'll be asked 
	
	which direction you'd like to move to.  Each floor space can either contain 
	
	a treasure chest, a shop, or a monster.  The floor boss will only appear 
	
	after clearing every monster on the floor on the bottom right corner of the 
	
	grid and a notification will let you know when the boss appears.\n"""
	
	characterSelection = 0
	position = (0,0)
	while(characterSelection != '1'):
		print "Select your class:"
		print "1: Warrior"
		characterSelection = raw_input('> ')
	if(characterSelection == '1'):
		mainCharacter = Player("Warrior")
		print "These are your character stats: "
		print "Strength:", mainCharacter.strength
		print "Dexterity:", mainCharacter.dexterity
		print "Intelligence:", mainCharacter.intelligence
		print "HP:", mainCharacter.HP
		print "MP:", mainCharacter.MP
		
	
	floor1 = Floor(1, mainCharacter)
	mainCharacter.newFloor()
	bossAppeared = False
	#Display the menu when character has spawned on the top left
	position = displayMenu(mainCharacter, position)
	
elif(menuSelection == '2'):
	sys.exit()




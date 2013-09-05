#Initial Setup
import sys
from random import randint
from Tower import Floor
from Character import Player
from Items import Item
#Game intro

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
	
	after clearing every monster on the floor on the top left corner of the grid

	and a notification will let you know when the boss appears.\n"""
	
	characterSelection = 0
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
		print "HP:", mainCharacter.hitPoints
		print "MP:", mainCharacter.magicPoints
		
	
	floor1 = Floor(1, mainCharacter)
	
elif(menuSelection == '2'):
	sys.exit()
	




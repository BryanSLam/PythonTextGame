#Base module for items

class Item(object):
	
	def __init__(self, item):
		self.item = item
		
		#if(item == ""):
		#	self.description = ""
		#	self.category = []
		#	self.effect = [] only if the item is usable or equipable
		#	self.sellValue = 
		
		#Categories are tuples with the first slot being it's category
		#and the 2nd slot having its class specific category if needed
		
		#For effects the odd positions of the array will be what stat 
		#its affecting, the evens will be the bonus it gives
		
		if(item == "Jelly"):
			self.description = "Slime poop that you picked off the floor"
			self.category = ['etc']
			self.effect = []
			self.sellValue = 3
		
		elif(item == "Potion"):
			self.description = "Strange red liquid, smells like butt hole"
			self.category = "use"
			self.effect = ["HP", 10]
			self.sellValue = 10
		
		elif(item == "Excalibur"):
			self.description = "wat"
			self.category = "equip"
			self.effect = ["Strength", 20]
			self.sellValue = 1000

		elif(item == "Small Sword"):
			self.description = "It's Nicky's sword, get it? Cause his thing..."
			self.category = "equip"
			self.effect = []
			self.sellValue = 50
			
			
			
			
			
			
			
			
			
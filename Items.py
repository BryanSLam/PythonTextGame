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
			self.effect = ["Strength", 20,"HP", 20]
			self.sellValue = 1000

		elif(item == "Small Sword"):
			self.description = "It's Nicky's sword, get it? Cause his thing..."
			self.category = "equip"
			self.effect = ["Strength", 10]
			self.sellValue = 50
			
		elif(item == "Scat"):
			self.descritpion = "Shop owners gonna get mad if you sell them poop"
			self.category = "etc"
			self.effect = []
			self.sellValue = -5
			
		elif(item == "Scat Sword"):
			self.description = "Poop sword"
			self.category = "equip"
			self.effect = ["Strength", 4, "HP", -5]
			self.sellValue = 25
			
		elif(item == "Floor Map"):
			self.description = "How did the shop owner get a hold of this map..."
			self.category = "use"
			self.effect = []
			self.sellValue = 1
			
			
			
from enum import Enum

class Unit(Enum):
	ML = 1
	G = 2
	
	
#____________Recipes____________

class Drink:
	def __init__(self, name, ingredients, method, tags=[], glass=None, base_spirit=None, full_method=None, typ=None, variants=[]):
		self.name = name
		self.ingredients = ingredients
		self.method = method
		self.tags = tags
		self.glass = glass
		self.base_spirit = base_spirit
		self.full_method = full_method
		self.typ = typ
		self.variants = variants
		
		
	def add_variant(self):
		pass
		
	def make_drink(self, quantity):
		for i in self.ingredients:
			pass
			
class FullMethod:
	def __init__(self):
		pass
		
		
		
		
#____________Stock____________

class Ingredient:
	def __init__(self, name: str, stock=0, variants=[]):
		self.name = name
		self.stock = stock
		self.unit = None
		self.variants = variants
		self.ideas = {}
		
		
	def add_variant(self, name: str, unit_size: int, tags=[], stock=0):
		new_variant = Variant(name, unit_size, self.unit, self, tags, stock)
		self.variants.append(new_variant)
	
	def add_idea(self):
		print(f"-- Adding idea to {self.name} --")
		title = input("Enter idea title: ")
		idea_check = True
		ingr_list = []
		while idea_check:
			new_ingr = input("Enter components for idea, or [Enter] to finish: ")
			if new_ingr == "":
				self.ideas[title] = ingr_list
				idea_check = False
				console.clear() 
			else:
				ingr_list.append(new_ingr)
		
class Variant:
	def __init__(self, name, unit_size, unit, parent, tags=[], stock=0):
		self.name = name
		self.unit_size = unit_size
		self.unit = unit
		self.parent = parent
		self.tags = tags
		self.stock = stock
		self.favourite = False
		self.house = False
		
		
		
class Spirit(Ingredient):
	def __init__(self, name, stock, variants): #remindner for default values
		super().__init__(name, stock, variants)
		self.unit = Unit.ML
		
		
class Soft(Ingredient):
	def __init__(self, name, stock, variants):
		super().__init__(name, stock, variants)
		self.unit = Unit.ML
		
class Fresh(Ingredient):
	def __init__(self, name, stock, variants):
		super().__init__(name, stock, variants)
		self.unit = Unit.G
		
class Garnish(Ingredient):
	def __init__(self, name, stock, variants):
		super().__init__(name, stock, variants)
		self.unit = Unit.G
		
		
		
		
		
class Glass:
	pass

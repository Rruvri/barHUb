import time
import console

class Customer:
	def __init__(self, name, descr, company=None):
		self.name = name
		self.descr = descr
		self.company = company
		self.notes = []
		self.favourites = []
	
	def add_note(self, note):
		self.notes.append(note)
	
	def add_fav(self, fav):
		self.favourites.append(fav)
		

def create_new_customer():
	name = input("Enter customer name: ")
	
	descr_check = True
	descr_list = []
	while descr_check:
		descr_point = input("Enter brief description point, or [Enter] to continue: ")
		if descr_point != "":
			descr_list.append(descr_point)
		else:
			descr_check = False
	
	company = input("Enter customer's company or occupation, or [Enter] to skip: ")
	if company == "":
		company = None
		
	new_customer = Customer(name, descr_list, company)
	return new_customer
			
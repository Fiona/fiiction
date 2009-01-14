"""
------------------------------------------
-- Fiiction								--
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Direction class
"""


class Direction:
	
	# "There are directions north, south ..."
	list_name = ""
	
	# Commands to accept
	commands = []
	
	# Travelling message
	travelling = ""
	
	# Examination message
	examination = ""
	
	connecting_room = None	  
	cant_travel = ""
	list = True
	
	
	# Constructor
	def __init__(self, room, list = True):
		
		# A string means it's a dead end
		if type(room) == type(""):
			self.cant_travel = room
		else:
			self.connecting_room = room
			
		self.list = list


# ----------------------------
# Default, built-in directions
# ----------------------------

class North(Direction):	   
	list_name = "north"	   
	commands = ["north", "n"]	 
	travelling = "You travel north..."	  
	examination = "There is an exit leading north."


class East(Direction):
	list_name = "east"
	commands = ["east", "e"]
	travelling = "You travel east..."
	examination = "There is an exit leading east."


class South(Direction):
	list_name = "south"
	commands = ["south", "s"]
	travelling = "You travel south..."
	examination = "There is an exit leading south."

	
class West(Direction):    
	list_name = "west"
	commands = ["west", "w"]    
	travelling = "You travel west..."
	examination = "There is an exit leading west."

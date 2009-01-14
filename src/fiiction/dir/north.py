"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Direction class
North
"""

from fiiction.dir import Direction

class North(Direction):
    
    list_name = "north"
    
    commands = ["north", "n"]
    
    travelling = "You travel north..."
    
    examination = "There is an exit leading north."
    
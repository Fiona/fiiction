"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Direction class
East
"""

from fiiction.dir import Direction

class East(Direction):
    
    list_name = "east"
    
    commands = ["east", "e"]
    
    travelling = "You travel east..."
    
    examination = "There is an exit leading east."
    
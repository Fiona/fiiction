"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Direction class
West
"""

from fiiction.dir import Direction

class West(Direction):
    
    list_name = "west"
    
    commands = ["west", "w"]
    
    travelling = "You travel west..."

    examination = "There is an exit leading west."
        
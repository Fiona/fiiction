"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Direction class
South
"""

from fiiction.dir import Direction

class South(Direction):
    
    list_name = "south"
    
    commands = ["south", "s"]
    
    travelling = "You travel south..."

    examination = "There is an exit leading south."
        
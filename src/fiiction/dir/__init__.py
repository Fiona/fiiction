"""
------------------------------------------
-- Fiiction                             --
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
    cant_travel = "";
    list = True
    
    
    # Constructor
    def __init__(self, room, list = True):
        
        # A string means it's a dead end
        if type(room) == type(""):
            self.cant_travel = room
        else:
            self.connecting_room = room
            
        self.list = list
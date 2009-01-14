"""
MY STARTING ROOM
"""
from fiiction.room_helpers import Cavern
from fiiction.dir import North



class start(Cavern):
    
    room_name = "a cave"
    
    room_init_description = """You fall into a small hole and end up in a cave.\n 
Don'task me, I just work here..."""
                            
    room_description = "It is a very dark cave. What else do you want?"
    
    def create_room(self):
        
        Cavern.create_room(self)        
        self.exits["north"] = North(self.game.rooms['second_room']);
        
        self.things["rock"] = self.game.things["rock"];
        

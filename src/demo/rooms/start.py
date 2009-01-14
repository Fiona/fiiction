"""
MY STARTING ROOM
"""
from fiiction.room.helpers import hCavern
from fiiction.dir.north import North



class start(hCavern):
    
    room_name = "a cave"
    
    room_init_description = """You fall into a small hole and end up in a cave.\n 
Don'task me, I just work here..."""
                            
    room_description = "It is a very dark cave. What else do you want?"
    
    def create_room(self):
        
        hCavern.create_room(self)        
        self.exits["north"] = North(self.game.rooms['second_room']);
        
        self.things["rock"] = self.game.things["rock"];
        
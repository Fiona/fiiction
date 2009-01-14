"""
Second room
"""
from fiiction.room.helpers import hCavern
from fiiction.dir.south import South


class second_room(hCavern):
    
    room_name = "another cave"
    
    room_init_description = ""
                            
    room_description = "This is a pretty shitty room."
    
    def create_room(self):
        
        hCavern.create_room(self)        
        self.exits ["south"] = South(self.game.rooms['start_room']);

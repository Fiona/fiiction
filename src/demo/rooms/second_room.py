"""
Second room
"""
from fiiction.room_helpers import Cavern
from fiiction.dir import South


class second_room(Cavern):
    
    room_name = "another cave"
    
    room_init_description = ""
                            
    room_description = "This is a pretty shitty room."
    
    def create_room(self):
        
        Cavern.create_room(self)        
        self.exits ["south"] = South(self.game.rooms['start_room']);

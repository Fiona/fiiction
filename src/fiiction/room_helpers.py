"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Helper room classes
Here are some classes to extend from to create
basic "default" rooms without much effort
"""
from fiiction.room import Room
from fiiction.dir import North, South, West, East

 
class Cavern(Room):
    
    room_name = "a cavern"
    
    def create_room(self):
        
        default_exit = "There's just a rocky cave wall that way."
        
        self.exits = {
                      "north" : North(default_exit, list=False),
                      "south" : South(default_exit, list=False),
                      "east" : East(default_exit, list=False),
                      "west" : West(default_exit, list=False)                      
                      }

"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Thing class
Basic item...
"""
from fiiction.game import Game


class Thing:
    
    thing_name = "My Thing"
    list_name = "a thing"
        
    thing_description = "Description of the room."
    
    list = True
    game = None
            
    def __init__(self, game_class):
        self.game = game_class
                        
    def describe(self):
        Game.output(self.thing_description)
        
    def __str__(self):
        return self.thing_name
    
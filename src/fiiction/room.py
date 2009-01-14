"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Room class
Deals with room stuff...
"""
from fiiction.game import Game


class Room:
    
    room_name = "My Room"
    room_init_description = "Initial description of the room when first entered."
    room_description = "Description of the room."

    things = {}
    
    exits = {}
    
    times_entered = 0
    
    game = None
            
    def __init__(self, game_class):
        self.game = game_class
                
    def create_room(self):
        pass
    
    def enter(self):
        
        if self.times_entered == 0 and self.room_init_description != "":
            Game.output(self.room_init_description + "\n")
        
        self.describe()
        Game.output("")
        self.describe_exits()
        self.list_items()
        
        self.times_entered += 1
           
           
    def describe(self):
        Game.output(self.room_description)
        
        
    def describe_exits(self):
        
        if len(self.exits) > 0:
        
            exit_build = []
        
            for direction in self.exits:
                if self.exits[direction].list == True:
                    exit_build.append(self.exits[direction].list_name)
            
            if len(exit_build) > 0:
                Game.output("There are exits %s" % ", ".join(exit_build))
            
                
    def list_items(self):
        
        if len(self.things) > 0:
            
            item_build = []
            
            for item in self.things:
                if self.things[item].list == True:
                    item_build.append(self.things[item].list_name)
            
            if len(item_build) > 0:
                Game.output("You can also see %s" % ", ".join(item_build))
                                
                    
    def __str__(self):
        return self.room_name
    
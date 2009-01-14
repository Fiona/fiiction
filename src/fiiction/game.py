"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Game class
Holds the main game module, the main game should
extend from this.
"""

from fiiction.parse import parse_command

class Game:
    
    game_name = "Fiiction Game"
    author = "Your Name Here"

    rooms = {}
    things = {}
    starting_room = None
    starting_items = []
    
    description = "Description of your game is displayed at the start"
    
    starting_message = "Message for the start of the game is displayed at the start"
    
    # set to true to quickly quit
    end_game = False
    
    current_input = ""
    current_room = None
    
    suppress_room_description = False
    

    # ------------------------------------------------

    
    def __init__(self):
        pass
    
    
    # ------------------------------------------------

    
    def start_game(self):
        "The function that starts off a game."
        
        # create exits, objects and whatever else we want to do
        for room_name in self.rooms:
            self.rooms[room_name].create_room()
            
        
        # first message
        Game.output(
                    ["Fiiction by Fiona Burrows",
                     "-------------------------",
                     "%s by %s" % (self.game_name, self.author),
                     "-------------------------",
                     self.description,
                     "",
                     "",
                     self.starting_message,
                     "-------------------------"]
                    )                
        
        # go to the first room ... or not
        if self.starting_room == None:
            Game.output("You have no starting room set!")
        else:        
            self.current_room = self.starting_room 
            self.starting_room.enter()
            self.game_loop()

       
    # ------------------------------------------------


    @classmethod
    def output(self, text_to_output):
        "Outputs text to the screen, accepts string or list."
        
        # Single strings
        if type(text_to_output) == type(""):
            print text_to_output
        # list of strings
        elif type(text_to_output) == type([]):
            for single_text in text_to_output:
                print single_text

           
    # ------------------------------------------------

            
    def game_loop(self):
        "Keeps running, keeps checking input and doing things with it."
        
        while self.end_game == False:
            
            self.current_input = raw_input("\n>>>").lower().strip()
            
            if self.current_input == "quit":
                self.end_game = True
            else:
                # parse input
                if self.current_input != "":
                    command_return = parse_command(self.current_input, self)
                
                    if command_return == False:
                        Game.output("I don't understand.")
                
                # room describe
                if self.suppress_room_description == False:
                    Game.output("\nYou are in %s" % self.current_room.room_name)            
                    self.current_room.describe_exits()
                    self.current_room.list_items()
        
                self.suppress_room_description = False           
            
        Game.output("Bye!")


    # ------------------------------------------------

         
    def move_to_room(self, room_to):
        
        room_to.enter()
        
        self.current_room = room_to
        self.suppress_room_description = True
        
                
    # ------------------------------------------------

        
    def __str__(self):
        return self.game_name
               
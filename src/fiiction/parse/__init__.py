"""
------------------------------------------
-- Fiiction                             --
------------------------------------------
-- Interactive fiction by Fiona Burrows --
------------------------------------------

Parser deals with commands
"""

import re


def parse_command(command, game):
    
    commands = command.strip().split()

    game.suppress_room_description = True

    # ------------
    # EXAMINATION
    # ------------
    regular_exp = re.compile(r"^(?:look|examine)(?: at| upon)?(?P<object> .*)?", re.IGNORECASE).match(command);
    
    if regular_exp != None:

        captured_object = regular_exp.group("object");
        
        # probably want the room
        if captured_object == None:
            
            game.suppress_room_description = False
            game.output(game.current_room.room_description)   
            return True
        
        # Want to look at something else
        else:
        
            captured_object = captured_object.strip();
            # is it an object?
            dir_command = check_command_is_thing(captured_object, game)
            
            if type(dir_command) == type(""):
                game.output(game.current_room.things[dir_command].thing_description)
                return True
            
            # is it a direction?
            dir_command = check_command_is_direction(captured_object, game)
            
            if type(dir_command) == type(""):
                game.output(game.current_room.exits[dir_command].examination)
                return True
        
            game.output("There's nothing to look at.")
        
        return True
    
    # ------------
    # TRAVELLING
    # ------------    
    else:
        
        dir_command = check_command_is_direction(commands[0], game)
        
        if type(dir_command) == type(""):
            
            # dead end?
            if game.current_room.exits[dir_command].connecting_room == None:
                game.output(game.current_room.exits[dir_command].cant_travel)
            else:
                game.output(game.current_room.exits[dir_command].travelling + "\n")
                game.move_to_room(game.current_room.exits[dir_command].connecting_room)
            
            return True
        
    return False
            
            
# ------------------------------------------------

# Check that whatever command we're given is a direction in
# the room or not and if so, return the exit key            
def check_command_is_direction(command, game):
    
    if len(game.current_room.exits) > 0:
        
        for exit in game.current_room.exits:
            
            if len(game.current_room.exits[exit].commands) > 0:
                
                for exit_comm in game.current_room.exits[exit].commands:
                    
                    if exit_comm == command:
                        
                        return exit
                    
    return False


            
# ------------------------------------------------

# Check that whatever command we're given is a thing
# in the room or not and if so, return the things key            
def check_command_is_thing(command, game):
    
    if len(game.current_room.things) > 0:
        
        for obj in game.current_room.things:
                    
            if game.current_room.things[obj].thing_name == command:
                        
                return obj
                    
    return False

  
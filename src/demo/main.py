from fiiction.game import Game

from rooms import start, second_room
from things import rock

class awesome_zone(Game):
    
    game_name = "THIS IS THE AWESOME ZONE"
    author = "Fiona"
    
    description = "awesomeest game in the world"
    
    starting_message = "woaaaaaaaaaaaaaaah wtf"
    
    
# create instance    
game = awesome_zone()

# create rooms
game.rooms = {
             "start_room"   : start.start(game),
             "second_room"  : second_room.second_room(game)
             }

# create objects
game.things = {
               "rock" : rock.rock(game)
               }

game.starting_room = game.rooms['start_room']

# start the game off
game.start_game()
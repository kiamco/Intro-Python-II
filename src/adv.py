from room import Room
from player import Player

from simple_chalk import chalk, green
from pick import pick

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", ["sword", "armor"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""", ["poison", "arrow", "shiled"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""", ["potion", "candy"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""", ['note']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def room_mapper(room_name):
    if room_name == "Outside Cave Entrance":
        return "outside"
    
    if room_name == "Foyer":
        return "foyer"
    
    if room_name == "Grand Overlook":
        return "overlook"
    
    if room_name == "Narrow Passage":
        return "narrow"
    
    if room_name == "Treasure Chamber":
        return "treasure"

def navigator(direction,player):
    current_room = room_mapper(player.room.name)
    if direction == "n":
        player.set_room(room[current_room].n_to)
        return player
    
    if direction == "s":
        return player.set_room(room[current_room].s_to)
    
    if direction == "e":
        player.set_room(room[current_room].e_to)
        return player
    
    if direction == "w":
        return player.set_room(room[current_room].w_to)   

def is_pickup(value,player):
    if value == 'y':
        options = player.room.items
        option = pick(options,"\n❓  Item list (hit SPACE to pick and ENTER to confirm)", multiselect=True, min_selection_count=1)
        
        # add item to player remove item from room
        for i in option:
            player.add_item(i[0])
            player.room.remove_item(i[0])
            
        print(f"\tPlayer now has the following items {chalk.yellow(player.items)}")

    else:
        return
        
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

if __name__ == "__main__":
    player = Player(room=room['outside'])

    start = True

    while start:
        # print(player)
        direction = input("\n❓  Which way do you want to go (n, s, e, w): ")
        
        try:
            print(navigator(direction ,player))
            
            pick_up = input("❓\tDo you want to pick up item (y/n): ")
            is_pickup(pick_up, player)
        except AttributeError:
            print(chalk.red("ERROR: "), "path not available")
            
            
        if direction == "q":
            print("GOOD GAME")
            break
        
        if player.room.name == "Treasure Chamber":
            print(chalk.green.bold("You found the treasure room but no treasure :("))
            break
        
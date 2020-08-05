from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
 "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# add items to rooms here 

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'])

# Write a loop that:

while True:
    # * Prints the current room name 
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    # If the user enters "q", quit the game

    print(player1.location)

    command = input("> ").split(',')

    if command[0] == 'q':
        print(f'May the odds be ever in your favor')
        break 
    elif command[0] == 'n':
        # check if player can move to north 
        # if there is, set that north room as the player's location 
        if hasattr(player1.location, 'n_to'): 
            player1 = Player(player1.location.n_to)
            print(f'Northward and onward!')
        else:
            print(f'You cannot go where there is nothing')
    elif command[0] == 's':
        if hasattr(player1.location, 's_to'): 
            player1 = Player(player1.location.s_to)
            print(f'Southward and onward!')
        else:
            print(f'You cannot go where there is nothing')
    elif command[0] == 'e': 
        if hasattr(player1.location, 'e_to'):  
            player1 = Player(player1.location.e_to)
            print(f'Eastward and onward!')
        else:
            print(f'You cannot go where there is nothing')
    elif command[0] == 'w':
        if hasattr(player1.location, 'w_to'): 
            player1 = Player(player1.location.w_to)
            print(f'Westward and onward!')
        else:
            print(f'You cannot go where there is nothing')

    ## put item logic here or in each elif? ideally here 
    ### check if new location has items (if items property length > 0) and if it does, list the items
    ### give user option to pick up items 
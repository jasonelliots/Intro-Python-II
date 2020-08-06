from room import Room
from player import Player
from item import Item
import textwrap

# if I circle back to this - update to have all commands accessible from any point - dont loop through items every room where there is items - make riddle to get past dragon - 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
 "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('gold', 'shiny'), Item('rocks', 'dusty')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('gold', 'shiny'), Item('rocks', 'dusty')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('rocks', 'dusty'), Item('rocks', 'dusty')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('treasure', 'shiny'), Item('rocks', 'dusty')]),
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


player1 = Player(room['outside'])

intro = '\n\nWelcome to the Mind Game. \n\nYou can move through the map by selecting one of the cardinal directions: n - s - e - w. Your mission is to find the treasure and return from the cave without being scorched to smitherines by the FIRE BREATHING DRAGON. To begin, you have only an apple, a sword, and your lucky socks. \n\nFair well and farewell. \n'

formatted_intro = textwrap.indent(text=intro, prefix='  ')

print(formatted_intro)


while True:

    print(f'\n Current location: {player1.location.name}\n {player1.location.description}')

    if player1.location.name == "Treasure Chamber":
        print("OH MY GOD A FIRE BREATHING DRAGON")
    
    if len(player1.location.items) > 0:

        itemCheck = True 
        while itemCheck == True: 
            print(f'{player1.location.print_items()}')
            print(f'{player1.print_items()}')

            command = input("\n What do you do? \n Options: \n get (item) \n drop (item) \n move on \n >>> ").split(' ')

            if command[0] == 'get':
                player1.get(command[1])
                player1.location.remove(command[1])
            elif command[0] == 'drop':
                player1.location.add(command[1], player1.items)
                player1.drop(command[1])
            else:
                itemCheck = False

  
    command = input("Where would you like to go?").split(',')

    if command[0] == 'q':
        print(f'May the odds be ever in your favor')
        break 
    elif command[0] == 'n':
        # add conditional with firebreathing dragon if location is narrow passage... build out riddle logic 
        if hasattr(player1.location, 'n_to'): 
            player1 = Player(player1.location.n_to)
            print(f'\nNorthward and onward!\n')
        else:
            print(f'You cannot go where there is nothing')
    elif command[0] == 's':
        if hasattr(player1.location, 's_to'): 
            player1 = Player(player1.location.s_to)
            print(f'\nSouthward and onward!\n')
        else:
            print(f'You cannot go where there is nothing')
    elif command[0] == 'e': 
        if hasattr(player1.location, 'e_to'):  
            player1 = Player(player1.location.e_to)
            print(f'\nEastward and onward!\n')
        else:
            print(f'You cannot go where there is nothing')
    elif command[0] == 'w':
        if hasattr(player1.location, 'w_to'): 
            player1 = Player(player1.location.w_to)
            print(f'\nWestward and onward!\n')
        else:
            print(f'\nYou cannot go where there is nothing\n')

 
### give user option to pick up items - method in class constructor? or can I just player1.items.append ? 
### give user option to drop items  - method in class constructor? 
  

### if need be get something that works and is functional first - then go back and refactor to specifications - for input use .split(' ') on input
 ### if time - add riddle to get past dragon at treasure room 
# Project 2: Text Based Adventure Game
# Created by: Andrew Johnson (andrew.johnson26@snhu.edu)
# TODO: Implement functionality to get an item

# Intro
intro = "'You are a lone traveler who has awoken in a foreign desert tavern with no memory of the recent past.\nUpon " \
        "exiting your tent, you encounter an absent-minded expert on archeology, who explains to you the mystic power\n" \
        "of the nearby ruins and what has recently disturbed them. You and your new ally must explore the area to\n" \
        "locate the source of the disturbance, then fix or destroy it.'"

# Establish Rooms
rooms = {
    'Tavern': {'east': 'Ruins'},
    'Ruins': {'north': 'Ruined Temple', 'east': 'Assassin Camp', 'west': 'Tavern', 'south': 'Hidden Caves'},
    'Ruined Temple': {'east': 'Throne Room', 'south': 'Ruins'},
    'Throne Room': {'west': 'Ruined Temple'},
    'Assassin Camp': {'north': 'Assassin Chief\'s Tent', 'west': 'Ruins'},
    'Assassin Chief\'s Tent': {'south': 'Assassin Camp'},
    'Hidden Caves': {'north': 'Ruins', 'east': 'Coward\'s Cavern'},
    'Coward\'s Cavern': {'west': 'Hidden Caves'}
}
room_items = {
    'Tavern': [],
    'Ruins': ['rusty sword'],
    'Ruined Temple': [],
    'Throne Room': [],
    'Assassin Camp': ['steel sword'],
    'Assassin Chief\'s Tent': ['key of suffering'],
    'Hidden Caves': ['widower bow'],
    'Coward\'s Cavern': ['key of prosperity']
}

# Scrapped, out of project scope
# room_mobs = {
#     'Tavern': ['Mean Drunk'],
#     'Ruins': ['Desert Wolves'],
#     'Ruined Temple': ['Disciples of Suffering'],
#     'Throne Room': ['The Sufferer'],
#     'Assassin Camp': ['Assassins'],
#     'Assassin Chief\'s Tent': ['Assassin Chief'],
#     'Hidden Caves': ['Spiders'],
#     'Coward\'s Cavern': ['Coward']
# }

# Player global variables
current_room = 'Tavern'  # Instantiate to starting location
inventory = []


def game_help():
    print('Goal\n')
    print('Collect the keys to gain access to the Throne Room\n Then, defeat The Sufferer!\n')

    print('Valid Commands\n')
    print('go [direction] (North, East, West, South)\n Goes to a room in the specified direction\n')
    print('get [item]\n Adds an item in the room to your inventory\n')
    print('attack [mob]\n Instigates a fight with a mob in the room\n')
    print('inventory\n Shows the player\'s current inventory')


def command():
    valid_commands = ['go', 'get', 'inventory']

    user_command = input('What would you like to do?\n')
    tokens = user_command.split()

    # Command validation/redirection
    if tokens[0] == 'help':
        game_help()
    elif tokens[0] == 'exit':
        print('Thanks for playing, goodbye!')
        exit()
    elif tokens[0] == 'inventory':
        print_inventory()
    elif len(tokens) != 2 or tokens[0] not in valid_commands:
        print('Invalid command -- try \'help\'')
    elif tokens[0] == 'go':
        go(tokens[1])


def go(direction):
    global current_room
    direction = direction.lower()
    if direction not in rooms[current_room]:
        print('There is nothing this way...')
    else:
        current_room = rooms[current_room][direction]


def print_inventory():
    for item in inventory:
        print(item)


while True:
    command()
    print('You have entered {}'.format(current_room))
    if current_room == 'Throne Room':
        print('You have reached the final room and defeated The Sufferer!\n')
        print('Thanks for playing, goodbye!')
        exit()

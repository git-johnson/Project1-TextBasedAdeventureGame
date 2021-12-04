
# Project 2: Text Based Adventure Game
# Created by: Andrew Johnson (andrew.johnson26@snhu.edu)

# Intro
intro = "'You are a lone traveler who has awoken in a foreign desert tavern with no memory of the recent past.\nUpon " \
        "exiting your tent, you encounter an absent-minded expert on archeology, who explains to you the mystic power\n" \
        "of the nearby ruins and what has recently disturbed them. You and your new ally must explore the area to\n" \
        "locate the source of the disturbance, then fix or destroy it.'"

# Establish Rooms
rooms = {
    'Tavern': {'East': 'Ruins'},
    'Ruins': {'North': 'Ruined Temple', 'East': 'Assassin Camp', 'West': 'Tavern', 'South': 'Hidden Caves'},
    'Ruined Temple': {'East': 'Throne Room', 'South': 'Ruins'},
    'Throne Room': {'West': 'Ruined Temple'},
    'Assassin Camp': {'North': 'Assassin Chief\'s Tent', 'West': 'Ruins'},
    'Assassin Chief\'s Tent': {'South': 'Assassin Camp'},
    'Hidden Caves': {'North': 'Ruins', 'East': 'Coward\'s Cavern'},
    'Coward\'s Cavern': {'West': 'Hidden Caves'}
}
room_items = {
    'Tavern': [],
    'Ruins': ['Rusty Sword'],
    'Ruined Temple': [],
    'Throne Room': [],
    'Assassin Camp': ['Steel Sword'],
    'Assassin Chief\'s Tent': ['Key of Suffering'],
    'Hidden Caves': ['Widower Bow'],
    'Coward\'s Cavern': ['Key of Prosperity']
}
room_mobs = {
    'Tavern': ['Mean Drunk'],
    'Ruins': ['Desert Wolves'],
    'Ruined Temple': ['Disciples of Suffering'],
    'Throne Room': ['The Sufferer'],
    'Assassin Camp': ['Assassins'],
    'Assassin Chief\'s Tent': ['Assassin Chief'],
    'Hidden Caves': ['Spiders'],
    'Coward\'s Cavern': ['Coward']
}

# Player global variables
current_room = 'Tavern'  # Instantiate to starting location
inventory = ['test']


def game_help():
    print('Goal\n')
    print('Collect the keys to gain access to the Throne Room\n Then, defeat The Sufferer!\n')

    print('Valid Commands\n')
    print('go [direction] (North, East, West, South)\n Goes to a room in the specified direction\n')
    print('get [item]\n Adds an item in the room to your inventory\n')
    print('attack [mob]\n Instigates a fight with a mob in the room\n')
    print('inventory\n Shows the player\'s current inventory')


def command():
    valid_commands = ['go', 'get', 'attack', 'inventory']
    
    user_command = input('Enter a command:\n')
    tokens = user_command.split()

    if tokens[0] == 'help':
        game_help()
        return
    elif tokens[0] == 'inventory':
        printInventory()
    elif len(tokens) != 2 or tokens[0] not in valid_commands:
        print('Invalid command -- try \'help\'')
    elif tokens[0] == 'go':
        go(tokens[1])
        


def go(direction):
    global current_room
    if direction not in rooms[current_room]:
        print('There is nothing this way...')
    else:
        current_room = str(rooms[direction])


def printInventory():
    for item in inventory:
        print(item)



while True:
    command()
    print(current_room)

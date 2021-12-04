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
    user_command = input('Enter a command:\n')
    user_command.split()

    if len(user_command) > 2:
        print('Too many arguments - type \'help\'')
    elif user_command[0] == 'go':
        user_command[1].lower()
        go(user_command[1], current_room)


def go(direction, current_room_param):
    if direction not in rooms[current_room_param]:
        print('There is nothing this way...')
    else:
        current_room = rooms[current_room_param][direction]


while True:
    command()

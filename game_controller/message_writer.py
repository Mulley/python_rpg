from constants.constants import FORK_IN_ROAD_MESSAGE


def start_message_pick_path(player):
    print("You are {}, the {}".format(player.name, player.class_type))
    print(FORK_IN_ROAD_MESSAGE)
    print("Which way do you go?")
    print("1. Left\n2. Right")
    print()
    while True:
        direction = input("Pick a path: ")
        if direction == '1':
            return 'Left'
        elif direction == '2':
            return 'Right'
        else:
            print('Not a valid input.')

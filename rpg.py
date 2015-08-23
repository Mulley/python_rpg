from game_controller.game_controller import character_create
from game_controller.battle import battle
from game_controller.message_writer import start_message_pick_path
from items.base_items import Potion
from characters.base_classes import Mage
from characters.enemy import Slime
from constants.constants import *


def main():

    player = character_create()
    potion = Potion()
    player.inventory.append(potion)
    friend = Mage("Dude")

    direction = start_message_pick_path(player)
    print()
    if direction == "Left":
        back = False
        while not back:
            slime = Slime()
            slime2 = Slime()

            print("Enemies Appear!")
            battle([player, friend, slime, slime2],
                   [player, friend], [slime, slime2])
            if player.hp > 0:
                print("Behind the beast was a dead end. Turn back?")
                print("1. Yes\n2. No")
                print()
                go_back = input("Go back? : ")
                if go_back == "1":
                    print(GO_BACK_MESSAGE)
                    back = True
                elif go_back == "2":
                    continue
            else:
                break
    elif direction == "Right":
        print(RIGHT_PATH_MESSAGE)
    print("Game over.")

if __name__ == '__main__':
    main()

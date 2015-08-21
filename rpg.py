from game_controller.game_controller import character_create
from game_controller.battle import battle
from items.base_items import Potion
from characters.base_classes import Mage
from characters.enemy import Slime


def main():

    player = character_create()
    potion = Potion()
    player.inventory.append(potion)
    friend = Mage("Dude")

    print("You are {}, the {}".format(player.name, player.class_type))
    print()
    print(
        "As you travel throught the forest you encounter a fork in the road.")
    print("Which way do you go?")
    print("1. Left\n2. Right")
    print()
    direction = input("Pick a path: ")
    print()
    if direction == "1":
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
                    print((
                        "As you head back you see another adventurer walking ",
                        " away from the other path with boundless treasure,",
                        " too bad you didn't go that way."
                        ))
                    back = True
                elif go_back == "2":
                    continue
            else:
                break
    elif direction == "2":
        print((
            "You discover boundless treasure and will never",
            " have to work another day of you life!"
            ))
    print("Game over.")

if __name__ == '__main__':
    main()

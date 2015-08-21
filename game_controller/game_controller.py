from characters.base_classes import Fighter, Mage, Rogue


def character_create():
    name = input("Hello brave adventurer, what is your name? : ")
    print()
    print("1. Fighter\n2. Mage\n3. Rogue")
    print()

    chosen = False
    while not chosen:
        class_choice = input("Please choose a class: ")
        print()
        if class_choice == "1":
            return Fighter(name)
            chosen = True
        elif class_choice == "2":
            return Mage(name)
            chosen = True
        elif class_choice == "3":
            return Rogue(name)
            chosen = True
        else:
            print("Invalid input. Please pick 1, 2, 3")
            continue


def turn_order(combatants):
    speed_order = sorted(
        combatants, key=lambda character: character.spd, reverse=True)

    return speed_order


def check_health(party):

    for person in party:
        if(person.hp > 0):
            return True

    return False


def pick_target(enemies):

    print("Which enemy do you target?")
    print()

    for idx, enemy in enumerate(enemies):
        print("{}. {} HP: {}".format(idx, enemy.name, enemy.hp))

    valid_target = False

    while not valid_target:
        target = input("Pick Target: ")
        try:
            target = int(target)
            valid_target = 0 <= target <= idx
        except ValueError:
            pass
        if not valid_target:
            print("Invalid Target")
    else:
        return target

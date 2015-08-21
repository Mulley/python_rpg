import random
from game_controller.game_controller import (turn_order,
                                             pick_target,
                                             check_health)


def battle(all_combatants, party, enemies):
    all_combatants = turn_order(all_combatants)

    party_alive = True
    enemies_alive = True

    enemies_defeated = []

    while party_alive and enemies_alive:

        print("*-------------------*")
        for person in party:
            print("{}'s HP: {}".format(person.name, person.hp))
            print("{}'s MP: {}".format(person.name, person.mp))
            print("-------------------")
        for enemy in enemies:
            print("{}s HP: {}".format(enemy.name, enemy.hp))
            print("{}s MP: {}".format(enemy.name, enemy.mp))
            print("-------------------")
        print("*-------------------*")
        print()

        for person in all_combatants:
            if person in party and person.hp > 0:
                print("{}'s Turn".format(person.name))
                print("1. Attack\n2. Magic Attack *MP Cost: 2*")
                print("3. Defend\n4. Use Item")

                valid_input = False

                while not valid_input:
                    choice = input("Enter command number: ")
                    valid_input = choice in ["1", "2", "3", "4"]
                    print()
                    if choice == "1":
                        player_target = pick_target(enemies)
                        print("You attack with your {}!".format(person.weapon))
                        person.basic_attack(enemies[player_target])
                        if enemies[player_target].hp <= 0:
                            enemies[player_target].hp = 0
                            print("{} defeated {}".format(
                                person.name, enemies[player_target].name))
                            enemies_defeated.append(enemies[player_target])
                            enemies.pop(player_target)
                    elif choice == "2":
                        if(person.mp >= 2):
                            player_target = pick_target(enemies)
                            print("You cast a ball of magic energy!")
                            person.magic_attack(enemies[player_target])
                            person.mp = person.mp - 2
                            if enemies[player_target].hp <= 0:
                                enemies[player_target].hp = 0
                                print("{} defeated {}".format(
                                    person.name, enemies[player_target].name))
                                enemies_defeated.append(enemies[player_target])
                                enemies.pop(player_target)
                        else:
                            print("You don't have enough mp for that!")
                            valid_input = False
                            continue
                    elif choice == "3":
                        print("You ready yourself for an attack.")
                        person.dfs = person.dfs * 1.5
                    elif choice == "4":
                        try:
                            print("Your inventory")
                            person.check_inventory()
                        except Exception:
                            print("You have no items.")
                            valid_input = False
                    else:
                        print("Input not recoginized!")
                        continue
                enemies_alive = check_health(enemies)
                if not enemies_alive:
                    break

            elif person in enemies and person.hp > 0:
                print("{}'s Turn".format(person.name))
                target = random.randrange(0, len(party))
                valid_target = party[target].hp > 0

                while not valid_target:
                    target = random.randrange(0, len(party))
                    valid_target = party[target].hp > 0
                else:
                    print("{} attacks {}".format(person.name,
                                                 party[target].name))
                    person.basic_attack(party[target])
                    target = random.randrange(0, len(party))

                party_alive = check_health(party)
                if not party_alive:
                    break

    else:
        if not party_alive and enemies_alive:
            print("You're party has died...")
        elif not enemies_alive and party_alive:
            print("All enemies have been defeated!")
            for person in party:
                person.calculate_experience(enemies_defeated)
                person.check_level_up()
        else:
            print("Double KO?")

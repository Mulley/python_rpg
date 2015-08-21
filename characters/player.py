from characters.base_character import Character


class Player(Character):

    """Create Player Class"""
    # initialize player at level 1 with 0 experience
    exp = 0
    lvl = 1

    def __init__(self):
        pass

    # define stats from base stats of subclass
    def stats_init(self):
        self.hp = self.stats['BASE_HP']
        self.mp = self.stats['BASE_MP']
        self.atk = self.stats['BASE_ATK']
        self.dfs = self.stats['BASE_DFS']
        self.magic_atk = self.stats['BASE_MAGIC_ATK']
        self.spd = self.stats['BASE_SPD']
        self.luck = self.stats['BASE_LUCK']

    # loop through base stats dict and add level up modifiers
    def level_up(self):
        print()
        print("*--- {} LEVELED UP! ---*".format(self.name))
        for stat, value in self.stats.items():
            print(
                "{}: {} + {} -->".format(stat, value, self.modifiers[stat]), end="")
            self.stats[stat] = value + self.modifiers[stat]
            print(self.stats[stat])
        self.lvl += 1
        print("*----------------------------------*")
        print()
        self.stats_init()

    # check level requirements and call level up on self if met
    def check_level_up(self):
        self.levels = [100, 250, 500, 1200]
        for value in self.levels:
            if self.exp >= value:
                self.level_up()
                self.levels.remove(value)
                break

    # take in enemies defeated from battle and add exp to total player
    # controlled character
    def calculate_experience(self, enemies):
        exp_gain = 0
        for enemy in enemies:
            self.exp = self.exp + enemy.exp
            exp_gain = exp_gain + enemy.exp
        print("{} gained {} exp!".format(self.name, exp_gain))
        print("{}'s total exp: {}".format(self.name, self.exp))

    def check_inventory(self):
        if len(self.inventory) > 0:
            for idx, item in enumerate(self.inventory):
                print("{}. {}".format(idx, item.name))

            valid_item = False
            while not valid_item:
                item = input("Pick an item: ")
                try:
                    item = int(item)
                    valid_item = 0 <= item <= idx
                except ValueError:
                    pass
                if not valid_item:
                    print("Invalid Target")
            else:
                self.inventory[item].use_potion(self)
        else:
            raise Exception("You have no items")

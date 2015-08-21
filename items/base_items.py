from items.item import Item


class Weapon(Item):

    """Define Weapon Item"""

    def __init__(self):
        self.type = "Weapon"


class Potion(Item):

    def __init__(self):
        self.name = "Healing potion"
        self.type = "Aid"
        self.short_desc = "Heals 5 HP"
        self.hp = 5

    def use_potion(self, user):
        print("{} used a potion!".format(user.name))
        if user.hp + self.hp < user.stats['BASE_HP']:
            user.hp = user.hp + self.hp
        else:
            user.hp = user.stats['BASE_HP']

from characters.player import Player

# TODO: create different class types


class Fighter(Player):

    """Defines Fighter Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Fighter"
        self.weapon = "sword"
        self.inventory = []
        self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10,
                      'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4, 'BASE_LUCK': 6}
        self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2,
                          'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1, 'BASE_LUCK': 1}
        self.stats_init()


class Mage(Player):

    """Defines Mage Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Mage"
        self.weapon = "wand"
        self.inventory = []
        self.stats = {'BASE_HP': 10, 'BASE_MP': 8, 'BASE_ATK': 5,
                      'BASE_DFS': 4, 'BASE_MAGIC_ATK': 12, 'BASE_SPD': 7, 'BASE_LUCK': 5}
        self.modifiers = {'BASE_HP': 2, 'BASE_MP': 4, 'BASE_ATK': 1,
                          'BASE_DFS': 3, 'BASE_MAGIC_ATK': 3, 'BASE_SPD': 2, 'BASE_LUCK': 1}
        self.stats_init()


class Rogue(Player):

    """Defines Rogue Class"""

    def __init__(self, name):
        self.name = name
        self.class_type = "Rogue"
        self.weapon = "dagger"
        self.inventory = []
        self.stats = {'BASE_HP': 10, 'BASE_MP': 4, 'BASE_ATK': 7,
                      'BASE_DFS': 4, 'BASE_MAGIC_ATK': 7, 'BASE_SPD': 10, 'BASE_LUCK': 10}
        self.modifiers = {'BASE_HP': 2, 'BASE_MP': 2, 'BASE_ATK': 2,
                          'BASE_DFS': 1, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 3, 'BASE_LUCK': 3}
        self.stats_init()

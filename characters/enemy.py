from characters.base_character import Character


class Enemy(Character):

    """Create Enemy"""

    def __init__(self):
        pass


class Slime(Enemy):

    """Create Beast Enemy"""

    def __init__(self):
        self.name = "Slime"
        self.hp = 10
        self.mp = 0
        self.atk = 7
        self.dfs = 4
        self.spd = 4
        self.luck = 1
        self.exp = 10

# monster.py
class Monster:
    def __init__(self, name, health, attack, defense, xp_reward, loot):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.loot = loot

    def attack(self, player):
        # Implement combat logic here
        pass

    def drop_loot(self):
        # Implement loot dropping logic here
        pass

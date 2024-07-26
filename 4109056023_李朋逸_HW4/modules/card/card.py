import random
from .names import get_first_name

class Card:
    def __init__(self, resource = 1, name = None, hp = None, attack = None, defense = None, ):
        self.record = {
            "name":     name if name else get_first_name(),
            "hp":       hp if hp else random.randint(8+2*resource,15+2*resource) * 50,
            "attack":   attack if attack else random.randint(8+3*resource,12+3*resource),
            "defense":  defense if defense else random.randint(5+2*resource,8+2*resource)
        }
    def __str__(self):
        s = """====================\nname: {}\nhp: {}\nattack: {}\ndefense: {}\n====================""".format(self["name"], self["hp"], self["attack"], self["defense"])
        return s
    def __repr__(self):
        return self["name"]
    def __getitem__(self, s):
        return self.record[s]
    def __setitem__(self, key, val):
        self.record[key] = val

    def levelUp(self):
        self["hp"] += 50
        self["attack"] += 1
        self["defense"] += 1


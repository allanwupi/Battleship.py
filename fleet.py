from enum import IntEnum
from random import randint

class Heading(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.symbol = name[0].upper()
        self.size = size
        self.health = size
        self.heading = Heading(randint(0,1))

class Fleet:
    _DEFAULT_FLEET = [
        Ship("Airship Carrier",5),
        Ship("Battleship",4),
        Ship("Cruiser",3),
        Ship("Submarine",3),
        Ship("Destroyer",2),
    ]
    
    def __init__(self, fleet=_DEFAULT_FLEET):
        self._ships = {}
        for s in fleet:
            self._ships[s.symbol] = s
    
    def describe(self):
        for k in self._ships:
            ship = self._ships[k]
            print(f'{k * ship.size:>6s}: {ship.name:15s} {ship.heading.name}')

    def damage(self, symbol):
        self._ships[symbol].health -= 1
        return self._ships[symbol].name, self._ships[symbol].health
    
    def ships(self):
        return self._ships.values()
    
    def keys(self):
        return self._ships.keys()


if __name__ == "__main__":
    print()
    my_fleet = Fleet()
    my_fleet.describe()
    print()
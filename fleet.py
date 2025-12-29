from enum import IntEnum
from random import randint

class Heading(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1

class Ship:
    def __init__(self, name, symbol, size):
        self.name = name
        self.symbol = symbol
        self.size = size
        self.health = size
        self.heading = Heading(randint(0,1))

class Fleet:
    _DEFAULT_FLEET = [
        Ship("Airship Carrier",'A',5),
        Ship("Battleship",'B',4),
        Ship("Cruiser",'C',3),
        Ship("Destroyer",'D',2),
        Ship("Submarine",'S',3),
    ]
    
    def __init__(self, fleet=_DEFAULT_FLEET):
        self._ships = {}
        self.total = 0
        for s in fleet:
            self._ships[s.symbol] = s
            self.total += s.size
    
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

PUZZLE_FLEET = [
    Ship("Battleship",'B',4),
    Ship("Cruiser",'C',3),
    Ship("Cruiser",'c',3),
    Ship("Destroyer",'D',2),
    Ship("Destroyer",'e',2),
    Ship("Destroyer",'f',2),
    Ship("Submarine",'s',1),
    Ship("Submarine",'t',1),
    Ship("Submarine",'u',1),
    Ship("Submarine",'v',1),
]


if __name__ == "__main__":
    print()
    my_fleet = Fleet()
    my_fleet.describe()
    print()
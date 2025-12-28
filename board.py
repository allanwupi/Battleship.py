from fleet import *
from random import randint

def chance(probability):
    roll = randint(1,100)
    return (probability >= roll)


class Board:
    def __init__(self, rows, cols, blank=' '):
        self.rows = rows
        self.cols = cols
        self.blank = blank
        # Directions: [0-HORIZONTAL, 1-VERTICAL]
        self.basis = [1, self.cols]
        self.vectors = [1, self.cols+1, self.cols, self.cols-1, -1, -self.cols-1, -self.cols, -self.cols+1]
        self.grid = [self.blank]*rows*cols
        self.fleet = Fleet()
        for ship in self.fleet.ships():
            self.spawn(ship)
    
    def render(self, hidden=False):
        row_idx = 1
        col_idx = ord('A')
        print('     ', end='')
        for j in range(self.cols):
            print(chr(col_idx) + ' ', end='')
            col_idx += 1
        print()
        print('   +-'+'--'*(self.cols)+'+')
        for i in range(self.rows):
            print(f'{row_idx:2d} | ',end='')
            for j in range(self.cols):
                pos = i*self.cols+j
                symbol = self.grid[pos]
                clear = '\033[0m'
                if symbol in self.fleet.keys():
                    if pos<self.rows*self.cols-1 and self.grid[pos+1] == symbol:
                        clear = ''
                    if hidden:
                        symbol = self.blank
                    else:
                        symbol = '\033[100m'+symbol
                print(clear+symbol+clear+' ', end='')
            print('\033[0m|')
            row_idx += 1
        print('   +-'+'--'*(self.cols)+'+')

    def shoot(self, i):
        if self.grid[i] != self.blank:
            ship_name, health = self.fleet.damage(self.grid[i])
            sequence = '\033[41m'+'X'+'\033[0m'
            print('Hit!')
            if health == 0:
                print(f"You sunk the enemy {ship_name}!")
        else:
            sequence = 'O'
            print('Miss.')
        self.grid[i] = sequence
    
    def out_of_bounds(self, i, j):
        return (i < 0 or j < 0 or i >= self.cols or j >= self.rows)

    def convert(self, coord):
        try:
            i = int(coord[1:])
            j = ord(coord[0].upper())
            i = int(i) - 1
            j = j - ord('A')
            if self.out_of_bounds(i, j):
                print(f"({i},{j}) is out of bounds")
                return None
            return i*self.cols + j
        except (ValueError, IndexError):
            print("Invalid move")
            return None
        
    def spawn(self, ship: Ship):
        start_col, end_col = 0,self.cols-1
        start_row, end_row = 0,self.rows-1
        if ship.heading == Heading.VERTICAL:
            end_row = self.rows-ship.size
        elif ship.heading == Heading.HORIZONTAL:
            end_col = self.cols-ship.size
        pos = None
        places = []
        while True:
            adjacent = False
            if pos is not None and chance(60):
                nearby = [pos+v for v in self.vectors if pos+v >= 0 and pos+v < self.rows*self.cols]
                for x in nearby:
                    if self.grid[x] != self.blank:
                        adjacent = True
                        break
            if (pos is None or self.grid[pos] != self.blank or adjacent):
                i = randint(start_row, end_row)
                j = randint(start_col, end_col)
                pos = i*self.cols+j
                places.clear()
                continue
            places.append(pos)
            pos += self.basis[ship.heading]
            if (len(places) >= ship.size):
                break
        for x in places:
            self.grid[x] = ship.symbol
    
    def game_over(self):
        total_health = 0
        for ship in self.fleet.ships():
            total_health += ship.health
        return (total_health == 0)


if __name__ == "__main__":
    print()
    game = Board(10,10,'\033[02m.\033[0m')
    game.render()
    print()
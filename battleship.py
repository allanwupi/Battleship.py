from board import *
import copy

EXIT_COMMANDS = ['', 'n', 'e', 'q','p','x','exit', 'clear', 'close', 'pass','quit']
CHEAT_CODES = ['r', 's', 'cheat', 'reveal', 'secret', 'show']
HINT_CODES = ['h', 'help', 'hint', 'hints']

def run():
    game = Board(10,10,'\033[2m.\033[0m')
    original = copy.deepcopy(game)
    player_move = ''
    turn_number = 1
    hints_used = 0
    game.render(True)
    while True:
        player_move = input(f"Turn {turn_number}: ")
        if player_move.lower() in EXIT_COMMANDS:
            break
        elif player_move.lower() in CHEAT_CODES:
            original.render()
            continue
        elif player_move.lower() in HINT_CODES:
            game.show_hints()
            game.render(hidden=True)
            hints_used += 1
            continue
        index = game.convert(player_move)
        if index is None:
            continue
        if game.grid[index] != game.blank and game.grid[index] not in game.fleet.keys():
            print('Already shot there.')
            continue
        else:
            game.shoot(index)
            game.render(hidden=True)
            if game.game_over():
                original.render()
                print(f"You destroyed the enemy fleet in {turn_number} turns.")
                print(f"Accuracy: {100*game.fleet.total/turn_number:.2f}%",end='')
                if (hints_used > 0):
                    print(f" (used {hints_used} hints).")
                else:
                    print()
                break
            turn_number += 1

if __name__ == "__main__":
    run()
from board import *
import copy

EXIT_COMMANDS = ['', 'n', 'e', 'c', 'q','p','x','exit', 'clear', 'close', 'pass','quit']
CHEAT_CODES = ['r', 's', 'cheat', 'reveal', 'secret', 'show']

if __name__ == "__main__":
    game = Board(10,10,'\033[2m.\033[0m')
    original = copy.deepcopy(game)
    player_move = ''
    turn_number = 1
    game.render(True)
    while True:
        player_move = input(f"Turn {turn_number}: ")
        if player_move.lower() in EXIT_COMMANDS:
            break
        if player_move.lower() in CHEAT_CODES:
            original.render()
            continue
        index = game.convert(player_move)
        if index is None:
            continue
        if game.grid[index] != game.blank and game.grid[index] not in game.fleet.keys():
            print('Already shot there.')
            continue
        else:
            game.shoot(index)
            game.render(True)
            if game.game_over():
                original.render()
                print(f"You destroyed the enemy fleet in {turn_number} turns.")
                break
            turn_number += 1
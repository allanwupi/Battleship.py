from game import *

EXIT_COMMANDS = ['', 'e', 'c', 'q','p','x','exit', 'clear', 'close', 'pass','quit']

if __name__ == "__main__":
    game = Board(10,10,'\033[2m.\033[0m')
    player_map = View(game)
    game.render()
    player_move = ''
    turn_number = 1
    while True:
        player_move = input(f"Turn {turn_number}: ")
        if player_move.lower() in EXIT_COMMANDS:
            break
        index = game.convert(player_move)
        if index is None:
            continue
        if game.grid[index] != game.blank and game.grid[index] not in game.fleet.keys():
            print('Already shot there.')
            continue
        else:
            game.shoot(index)
            player_map.render()
            turn_number += 1
        if game.game_over():
            print("The enemy fleet has been destroyed.")
            print(f"You win! Took {turn_number} turns.")
            break
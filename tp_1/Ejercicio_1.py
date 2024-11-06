import sys
from collections import deque

player_1 = "Sophia"
player_2 = "Mateo"

def main():

    check_argument_count()
    file = take_filename_argument()

    coins = extract_coins_data_from_file(file)

    winner = play_the_game(coins)
    return winner


def check_argument_count():
    if (len(sys.argv) !=2):
        print("Falta el nombre de archivo con los datos")
        sys.exit(1)

def take_filename_argument():
    return sys.argv[1]

def extract_coins_data_from_file(file):
    coins = []
    try:
        with open(file, 'r') as data_file:
            next(data_file)
            for line in data_file:
                line = line.strip()
                coins_data = line.split(";")
                for coin in coins_data:
                    coins.append(int(coin))
        return coins
    except FileNotFoundError:
        print(f"Error: El archivo '{file}' no existe.")
        sys.exit(1)

def play_the_game(coins):
    player_1_points = 0
    player_2_points = 0
    while coins:
        player_1_points += sophia_play_taking_higher_coin(coins)
        player_2_points += mateo_play_taking_lowest_coin(coins)
    return player_1 if player_1_points>player_2_points else player_2

def sophia_play_taking_higher_coin(coins):
    if coins[0]>coins[-1]:
        return coins.pop(0)
    else:
        return coins.pop()

def mateo_play_taking_lowest_coin(coins):
    if coins:
        if coins[0]>coins[-1]:
            return coins.pop()
        else:
            return coins.pop(0)
    return 0
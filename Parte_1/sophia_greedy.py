import sys
from collections import deque

player_1 = "Sophia"
player_2 = "Mateo"

PRIMERA = "Primera"
ULTIMA = "Última"

#Funcion que obtiene las monedas que deben seleccionar los jugadores Sophia y Mateo
#Pre: obtiene por parametro el nombre del archivo con las monedas
#Post: devuelve las monedas que deben seleccionar Sophia y Mateo, cada uno en una lista diferente,
#      y la suma de las monedas que selecciono cada uno.
#      [monedas Sophia], [monedas Mateo], suma Sophia, suma Mateo
def main():
    check_argument_count()
    file = take_filename_argument()

    coins = extract_coins_data_from_file(file)

    sophia_coins, mateo_coins = greedy_strategy(coins)
    
    show_result(sophia_coins, mateo_coins)
    
    return 0


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


#Funcion que obtiene las monedas que debe seleccionar Sophia y mateo en orden de turno,
#para que Sophia obtenga el maximo aculumado posible
#Pre: lista con las monedas del juego
#Post: lista con las monedas de Sopia, listas con la monedas de Mateo
def greedy_strategy(coins):
    sophia_coins = []
    mateo_coins = []
    while coins:
        sophia_play_taking_higher_coin(coins, sophia_coins)
        mateo_play_taking_lowest_coin(coins, mateo_coins)
    return sophia_coins, mateo_coins

def sophia_play_taking_higher_coin(coins, sophia_coins):
    if coins[0]>=coins[-1]:
        sophia_coins.append((coins.pop(0), PRIMERA))
    else:
        sophia_coins.append((coins.pop(), ULTIMA))

def mateo_play_taking_lowest_coin(coins, mateo_coins):
    if coins:
        if coins[0]>=coins[-1]:
            mateo_coins.append((coins.pop(), ULTIMA))
        else:
            mateo_coins.append((coins.pop(0), PRIMERA))


def show_result(sophia_coins, mateo_coins):
    for i in range(len(mateo_coins)):
        print(f"{sophia_coins[i][1]} moneda para {player_1}: {sophia_coins[i][0]};", end=" ")
        print(f"{mateo_coins[i][1]} moneda para {player_2}: {mateo_coins[i][0]};", end=" ")
    if len(sophia_coins) > len(mateo_coins):
        print(f"{player_1} toma la {sophia_coins[-1][1]} moneda {sophia_coins[-1][0]}", end=" ")
    print()
    print(f"Ganancia de Sophia: {sum(num for num, _ in sophia_coins)}")

main()

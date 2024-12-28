import sys
from collections import deque

player_1 = "Sophia"
player_2 = "Mateo"

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
    
    print("Valor total de las monedas elegidas por Sophia: ", sum(sophia_coins))
    print("Valor total de las monedas elegidas por Mateo: ", sum(mateo_coins))
    
    return sophia_coins, mateo_coins, sum(sophia_coins), sum(mateo_coins)


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
        sophia_coins.append(coins.pop(0))
    else:
        sophia_coins.append(coins.pop())

def mateo_play_taking_lowest_coin(coins, mateo_coins):
    if coins:
        if coins[0]>=coins[-1]:
            mateo_coins.append(coins.pop())
        else:
            mateo_coins.append(coins.pop(0))


main()

import sys


#Funcion que obtiene las monedas que deben seleccionar los jugadores Sophia y Mateo
#Pre: obtiene por parametro el nombre del archivo con las monedas
#Post: devuelve las monedas que deben seleccionar Sophia y Mateo, cada uno en una lista diferente,
#      y la suma de las monedas que selecciono cada uno.
#      [monedas Sophia], [monedas Mateo], suma Sophia, suma Mateo
def main():

    check_argument_count()
    file = take_filename_argument()

    coins = extract_coins_data_from_file(file)

    optimal_info = optimal_strategy(coins)
    sophia_choices, mateo_choices = reconstruction(coins, optimal_info)
    return sophia_choices, mateo_choices, sum(sophia_choices), sum(mateo_choices)


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


#Funcion que calcula el maximo acumulado de monedas para Sophia,
#en los subconjuntos posibles de monedas
#Pre: lista con las monedas del juego
#Post: matriz con los maximos para cada subconjunto de j-i+1 monedas
def optimal_strategy(coins):
    n = len(coins)
    dp_sophia = [[0 for _ in range(n)] for _ in range(n)]
    
    # Caso Base
    for i in range(n):
        dp_sophia[i][i] = coins[i]

    is_odd = n % 2

    for length in range(2+ is_odd, n+1, 2):
        for i in range(n - length + 1):
            j = i + length - 1
            # ecuacion de recurrencia
            dp_sophia[i][j] = max(coins[i] + (dp_sophia[i+2][j] if i+2 <= j and coins[i+1] >= coins[j] else dp_sophia[i+1][j-1]),
                                  coins[j] + (dp_sophia[i][j-2] if j-2 >= i and coins[j-1] > coins[i] else dp_sophia[i+1][j-1]))

    return dp_sophia


#Funcion que reconstruye las monedas que toma Sophia y Mateo en cada turno, ordenadas por orden cronologico
#Pre: lista de coins con las monedas
#     dp_sophia con la matriz de decisiones optimas de Sophia
#Post: lista de monedas que toma Sophia y Mateo en cada turno
def reconstruction(coins, dp_sophia):
    i = 0
    j = len(coins) - 1
    sophia_choices = []
    mateo_choices = []

    while i <= j:
        #caso borde
        if i==j:
            sophia_choices.append(coins[i])
            break

        choose_first = coins[i] + (dp_sophia[i+2][j] if i+2 <= j and coins[i+1] >= coins[j] else dp_sophia[i+1][j-1]) >= \
                       coins[j] + (dp_sophia[i][j-2] if j-2 >= i and coins[j-1] > coins[i] else dp_sophia[i+1][j-1])

        if choose_first:
            sophia_choices.append(coins[i])
            if i+2 <= j and coins[i+1] >= coins[j]:
                mateo_choices.append(coins[i+1])
                i += 2 #agarra mateo salteo [i+1]
            else:
                i += 1
                mateo_choices.append(coins[j])
                j -= 1 #agarra mateo salteo [j]
        else:
            sophia_choices.append(coins[j])
            if j-2 >= i and coins[j-1] > coins[i]:
                mateo_choices.append(coins[j-1])
                j -= 2 #agarra mateo salteo [j-1]
            else:
                mateo_choices.append(coins[i])
                i += 1 #agarra mateo salteo [i]
                j -= 1 

    return sophia_choices, mateo_choices



def util_sophia_measure(coins):
    optimal_info = optimal_strategy(coins)
    sophia_choices, mateo_choices = reconstruction(coins, optimal_info)
    return

main()

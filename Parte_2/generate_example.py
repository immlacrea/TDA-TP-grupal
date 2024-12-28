#Generacion de nuestros propios ejemplos de ejecucion

import random
import sophia_dinamica as pd
MIN_VALUE_COIN = 1
MAX_VALUE_COIN = 1000

def generate_random_coins(n, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(n)]


def write_results_to_file(sophia_choices, mateo_choices, filename="ejemplo_de_ejecucion_resultados.txt"):
    with open(filename, "w") as f:
        min_length = min(len(sophia_choices), len(mateo_choices))
        
        for i in range(min_length):
            f.write(f"Sophia agarra ({sophia_choices[i]}), Mateo agarra ({mateo_choices[i]})\n")
       
        f.write(f"Ganancia de Sophia: {sum(sophia_choices)}\n")
        f.write(f"Ganancia de Mateo: {sum(mateo_choices)}")


def write_coins_to_file(random_coins, filename="random_coins.txt"):
    with open(filename, "w") as f:
        for i in range(len(random_coins)):
            f.write(f"{random_coins[i]};")

def generar_ejemplos_de_ejecucion():

    # Ejemplo de uso
    n = 10  # Numero de monedas del arreglo
    random_coins = generate_random_coins(n, MIN_VALUE_COIN, MAX_VALUE_COIN)
    print("Random coins: ", random_coins)

    dp_sophia = pd.optimal_strategy(random_coins)
    sophia_choices, mateo_choices = pd.reconstruction(random_coins, dp_sophia)

    write_coins_to_file(random_coins)
    write_results_to_file(sophia_choices, mateo_choices)
    print("Archivo 'ejemplo_de_ejecucion_resultados.txt' creado correctamente")

generar_ejemplos_de_ejecucion()






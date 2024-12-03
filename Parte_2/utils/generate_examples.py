#Generacion de nuestros propios ejemplos de ejecucion
import random
import sophia_dinamica as pd


def generate_random_coins(n, min_value=1, max_value=1000):
    return [random.randint(min_value, max_value) for _ in range(n)]

def write_results_to_file(sophia_choices, mateo_choices, filename="resultados.txt"):
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

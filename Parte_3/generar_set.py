import random
import aproximacion_greedy as greedy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


MIN_TABLEROS = 1
MAX_TABLEROS = 301

def agregar_barcos_aletoriamente(barcos, n):
    cantidad_barcos = 3 * n

    for _ in range(cantidad_barcos):
        barcos.append(random.randint(1, n))
    return barcos

def generar_matriz_con_barcos(n, barcos):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    restricciones_fila = [0 for _ in range(n)]
    restricciones_columna = [0 for _ in range(n)]
    barcos_colocados = []

    def casilla_esta_vacia(fila,columna):
        return matriz[fila][columna] == 0

    def es_posicion_valida(fila, columna):
        # verifica que la fila y columna estee dentro de los limites de la matriz
        return 0 <= fila < n and 0 <= columna < n

    def es_adyacente_vacio(fila, columna):
        for desplazamiento_fila in [-1, 0, 1]:
            for desplazamiento_columna in [-1, 0, 1]:
                if desplazamiento_fila == 0 and desplazamiento_columna == 0:
                    continue
                f, c = fila + desplazamiento_fila, columna + desplazamiento_columna
                if es_posicion_valida(f, c) and not casilla_esta_vacia(f,c):
                    return False
        return True

    def puede_colocar_barco(fila, columna, longitud, horizontal):
        if horizontal:
            if columna + longitud > n:
                return False
            for c in range(columna, columna + longitud):
                if matriz[fila][c] != 0 or not es_adyacente_vacio(fila, c):
                    return False
        else:
            if fila + longitud > n:
                return False
            for f in range(fila, fila + longitud):
                if matriz[f][columna] != 0 or not es_adyacente_vacio(f, columna):
                    return False
        return True

    def colocar_barco(fila, columna, longitud, horizontal):
        if horizontal:
            for c in range(columna, columna + longitud):
                matriz[fila][c] = 1
                restricciones_fila[fila] += 1
                restricciones_columna[c] += 1
        else:
            for f in range(fila, fila + longitud):
                matriz[f][columna] = 1
                restricciones_fila[f] += 1
                restricciones_columna[columna] += 1

    for longitud_barco in barcos:
        colocado = False
        intentos = 0
        #Intentamos 100 veces colocar el barco en una posicion aletoria
        while not colocado and intentos < 10000:
            fila = random.randint(0, n - 1)
            columna = random.randint(0, n - 1)
            horizontal = random.choice([True, False])
            if puede_colocar_barco(fila, columna, longitud_barco, horizontal):
                colocar_barco(fila, columna, longitud_barco, horizontal)
                barcos_colocados.append(longitud_barco)
                colocado = True
            intentos += 1
        

    return matriz, restricciones_fila, restricciones_columna, barcos_colocados

def mostrar_tablero_en_consola(matriz, restricciones_fila, restricciones_columna, barcos_colocados,n):
    print("Tablero", n, "x", n , "generado:")
    print("Restricciones por fila:", restricciones_fila)
    print("Restricciones por columna:", restricciones_columna)
    print("Barcos colocados:", barcos_colocados)
    print("\nSolucion optima para el tablero:")
    for fila in matriz:
        print(" ".join(["B" if celda == 1 else "-" for celda in fila]))
    
    

def calcular_cota_tablero(n):
    barcos = agregar_barcos_aletoriamente([], n)
    matriz, restricciones_fila, restricciones_columna, barcos_colocados = generar_matriz_con_barcos(n, barcos)
    
    mostrar_tablero_en_consola(matriz, restricciones_fila, restricciones_columna, barcos_colocados,n)


    optimo_demandas_cumplidas = sum(restricciones_fila) + sum(restricciones_columna)
    
    barcos = agregar_barcos_aletoriamente(barcos_colocados.copy(), n)
    random.shuffle(barcos)
    
    table, demandas_filas_no_cumplidas, demandas_columnas_no_cumplidas = greedy.aprox_sea_battle(restricciones_fila, restricciones_columna, barcos)
    print("\nLeyenda del tablero",n,"x",n,"para la solucion greedy:")
    print("0: Casilla valida")
    print("1: Casilla invalida")
    print("2: Barco")

    print("Solucion greedy del tablero:")  
    for row in table:
        print(row)
    print("Restricciones que no se pudieron cubir por fila",demandas_filas_no_cumplidas )
    print("Restricciones que no se pudieron cubir por columna",demandas_columnas_no_cumplidas)
    print(n)

    demandas_totales_no_cumplidas = demandas_filas_no_cumplidas + demandas_columnas_no_cumplidas
    total_demandas_cumplidas_greedy = optimo_demandas_cumplidas - demandas_totales_no_cumplidas
    print("\n--------------------------------------------------\n")
    return total_demandas_cumplidas_greedy / optimo_demandas_cumplidas

cotas = [calcular_cota_tablero(n) for n in range(MIN_TABLEROS, MAX_TABLEROS)]
peor_cota = min(cotas)

print(f"\nLa peor cota es: {peor_cota}")
    

n_values = list(range(MIN_TABLEROS, MAX_TABLEROS))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(n_values, cotas, marker='o', linestyle='-', color='b', label='Cota obtenida')
plt.title('Cota obtenida para cada tamaño de tablero')
plt.xlabel('Tamaño del tablero (n)')
plt.ylabel('Cota obtenida')
plt.grid(True, linestyle='--', alpha=0.6)
min_index = cotas.index(min(cotas))
min_tick = n_values[min_index]
ticks = [n_values[0], n_values[len(n_values) // 2], n_values[-1], min_tick]
plt.scatter([min_tick], [min(cotas)], color='red', label='Cota mínima', zorder=5) #resaltar el minimo
plt.xticks(ticks, labels=[str(t) for t in ticks])
plt.xticks(n_values)
plt.legend()
plt.show() 







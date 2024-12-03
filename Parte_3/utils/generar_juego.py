import random

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
        while not colocado and intentos < 100:
            fila = random.randint(0, n - 1)
            columna = random.randint(0, n - 1)
            horizontal = random.choice([True, False])
            if puede_colocar_barco(fila, columna, longitud_barco, horizontal):
                colocar_barco(fila, columna, longitud_barco, horizontal)
                barcos_colocados.append(longitud_barco)
                colocado = True
            intentos += 1
        if not colocado:
            print(f"No se pudo colocar el barco de longitud {longitud_barco}")

    return matriz, restricciones_fila, restricciones_columna, barcos_colocados

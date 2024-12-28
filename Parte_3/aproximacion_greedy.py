#Aproximacion Greddy de John Jellicoe 
import sys
VALID = 0
NOT_VALID = 1
SHIP = 2

COLUMN = 1
ROW = 0

#Funcion que resuelve aproximadamente el problema del juego de la batalla naval solitaria
#Pre: obtiene por parametro el nombre del archivo con las monedas
#Post: devuelve el tablero con la solucion aproximada, 
#       la cantidad de demandas no cumplidas en las filas y en las columnas
def main():
    check_argument_count()
    file = take_filename_argument()

    row_demands, column_demands, ships = extract_game_data_from_file(file)

    table, row_unfulfilled_demands, column_unfulfilled_demands = aprox_sea_battle(row_demands, column_demands, ships)
    print("\nLeyenda del tablero:")
    print("0: Casilla valida")
    print("1: Casilla invalida")
    print("2: Barco")

    print("Solucion greedy del tablero:")  
    for row in table:
        print(row)
    print("Restricciones que no se pudieron cubir por fila",row_unfulfilled_demands )
    print("Restricciones que no se pudieron cubir por columna",column_unfulfilled_demands)

    return table, row_unfulfilled_demands, column_unfulfilled_demands


def check_argument_count():
    if (len(sys.argv) !=2):
        print("Falta el nombre de archivo con los datos")
        sys.exit(1)

def take_filename_argument():
    return sys.argv[1]

def extract_game_data_from_file(file):
    row_demands = [] 
    column_demands = []
    ships = []
    try:
        with open(file, 'r') as data_file:
            next(data_file)
            next(data_file)
            while True:
                line = data_file.readline().strip()
                if not line:
                    break
                row_demands.append(int(line))

            while True:
                line = data_file.readline().strip()
                if not line:
                    break
                column_demands.append(int(line))

            while True:
                line = data_file.readline().strip()
                if not line:
                    break
                ships.append(int(line))
        return row_demands, column_demands, ships
    except FileNotFoundError:
        print(f"Error: El archivo '{file}' no existe.")
        sys.exit(1)


def aprox_sea_battle(row_demand, column_demand, ships):
    table = create_table(row_demand, column_demand)
    row_demand_remaining = row_demand.copy()
    column_demand_remaining = column_demand.copy()
    ships_remaining = ships_remaining = sorted(ships, reverse=True)

    #Se utilizan dos demandas aux para poder diferenciar las demandas en las que no entró un barco
    #para sacarla de la proxima busqueda de max demanda
    row_demands_aux = row_demand.copy()
    column_demands_aux = column_demand.copy()
    (bigger_demand, index, is_column) = calculate_bigger_demand(row_demands_aux, column_demands_aux)

    while ships_remaining and bigger_demand:
        a_ship_is_placed = False
        for ship in ships_remaining:
            if ship_not_enter_in_demand(bigger_demand, ship):
                continue
            width_start = find_valid_position(table, row_demand_remaining, column_demand_remaining, index, is_column, ship)
            if position_not_valid(width_start):
                continue
            put_ship_in_table(table, row_demand_remaining, column_demand_remaining, index, width_start, is_column, ship)
            ships_remaining.remove(ship)
            a_ship_is_placed = True
            break
        if a_ship_is_placed:
            column_demands_aux = column_demand_remaining.copy()
            row_demands_aux = row_demand_remaining.copy()
        else:
            deny_demand(row_demands_aux, column_demands_aux, index, is_column)
        (bigger_demand, index, is_column) = calculate_bigger_demand(row_demands_aux, column_demands_aux)
    
    row_unfulfilled_demands = sum(row_demand_remaining)
    column_unfulfilled_demands = sum(column_demand_remaining)
    return table, row_unfulfilled_demands, column_unfulfilled_demands


def create_table(row_demand, column_demand):
    table = [ [VALID for i in range(len(column_demand))] for j in range(len(row_demand)) ]
    return table


def calculate_bigger_demand(row_demand_remaining, column_demand_remaining):
    index_big_row, big_elemt_row = get_bigger_element_info(row_demand_remaining)
    index_big_column, big_elemt_column = get_bigger_element_info(column_demand_remaining)
    return (big_elemt_row, index_big_row, ROW) if big_elemt_row >= big_elemt_column else (big_elemt_column,index_big_column, COLUMN)

def get_bigger_element_info(array):
    max = array[0]
    index = 0
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
            index = i
    return index, max

def ship_not_enter_in_demand(demand, ship):
    return ship > demand



def find_valid_position(table, row_demands, column_demands, lenght_index, is_column, ship):
    width_demands = row_demands if is_column else column_demands
    posible_contiguous_space = 0
    index = 0
    while index<len(width_demands) and posible_contiguous_space < ship:
        position_status = table[index][lenght_index] if is_column else table[lenght_index][index]
        if width_demands[index] >= 1 and position_status == VALID:
            posible_contiguous_space += 1
        else:
            posible_contiguous_space = 0
        index += 1
    return index-posible_contiguous_space if posible_contiguous_space == ship else -1

def position_not_valid(width_start):
    return width_start == -1



def put_ship_in_table(table, row_demands, column_demands, lenght_index, width_index, is_column, ship):
    update_demands(row_demands, column_demands, lenght_index, width_index, is_column, ship)
    update_table(ship, table, lenght_index, width_index, is_column)

def update_demands(row_demands, column_demands, lenght_index, width_index, is_column, ship):
    notify_width_demands(row_demands, column_demands, width_index, is_column, ship)
    notify_lenght_demands(row_demands, column_demands, lenght_index, is_column, ship)
    
def notify_width_demands(row_demands, column_demands, width_index, in_rows, ship):
    for i in range(width_index, width_index+ship):
        if in_rows:
            row_demands[i] -= 1
        else:
            column_demands[i] -= 1

def notify_lenght_demands(row_demands, column_demands, lenght_index, is_column, ship):
    if is_column:
        column_demands[lenght_index] -= ship
    else:
        row_demands[lenght_index] -= ship


def update_table(ship, table, lenght_index, width_index, is_column):
    for i in range( max(0, width_index), min(width_index+ship+1, len(table)) ):
        for j in range( max(0, lenght_index-1), min(lenght_index+2, len(table[0]) )):
            if is_column:
                if (j == lenght_index) and (width_index <= i < width_index+ship):
                    table[i][j] = SHIP
                else:
                    table[i][j] = NOT_VALID
            else:
                if (j == lenght_index) and (width_index <= i < width_index+ship):
                    table[j][i] = SHIP
                else:
                    table[j][i] = NOT_VALID


def deny_demand(row_demands, column_demands, index, is_column):
    if is_column:
        column_demands[index] = 0
    else:
        row_demands[index] = 0

if __name__ == "__main__":
    main()
# (0.75 Parte 1)
# Se pedirá al usuario el número de filas y columnas de una matriz. Se supone que los números introducidos son correctos.
# Una vez pedidos se llamará a la función GenerarMatrizSimple.

# Función GenerarMatrizSimple: Esta función recibirá como parámetros el número de filas y columnas.

# Generar una matriz con números aleatorios entre 1 y 50.
# Los números sí se pueden repetir en la matriz.
# Mostrar la matriz generada.
# Devolver la matriz generada.



# (0.75 Parte 2)
# Se le pedirá al usuario un número a buscar en la matriz. Después se llamará a la función BuscarYReemplazar.

# Función BuscarYReemplazar: Esta función recibirá como parámetros la matriz y el número a buscar:

# Buscar todas las posiciones donde aparece ese número en la matriz.
# Si el número se encuentra:

# Mostrar todas las posiciones donde aparece (fila, columna)
# Contar cuántas veces aparece
# Reemplazar todas las apariciones por el número 99
# Mostrar la matriz modificada


# Si el número no se encuentra:

# Mostrar el mensaje "Número no encontrado en la matriz"
# Mostrar qué números sí aparecen en la matriz (sin repetir)
import random

def GenerarMatrizSimple(filas, columnas):
    # """Genera una matriz con números aleatorios entre 1 y 50"""
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero_aleatorio = random.randint(1, 50)
            fila.append(numero_aleatorio)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    # """Muestra la matriz de forma ordenada"""
    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)

def BuscarYReemplazar(matriz, numero_a_buscar):
    # """Busca un número en la matriz y lo reemplaza por 99"""
    posiciones = []
    
    # Buscar todas las posiciones donde aparece el número
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero_a_buscar:
                posiciones.append((i, j))
    
    if posiciones:
        # Si se encuentra el número
        print(f"\nNúmero {numero_a_buscar} encontrado en las siguientes posiciones:")
        for pos in posiciones:
            print(f"Fila {pos[0]}, Columna {pos[1]}")
        
        print(f"\nEl número {numero_a_buscar} aparece {len(posiciones)} veces")
        
        # Reemplazar todas las apariciones por 99
        for pos in posiciones:
            matriz[pos[0]][pos[1]] = 99
        
        print("\nMatriz después del reemplazo:")
        mostrar_matriz(matriz)
    else:
        # Si no se encuentra el número
        print(f"\nNúmero {numero_a_buscar} no encontrado en la matriz")
        
        # Mostrar qué números sí aparecen (sin repetir)
        numeros_unicos = set()
        for fila in matriz:
            for numero in fila:
                numeros_unicos.add(numero)
        
        numeros_ordenados = sorted(list(numeros_unicos))
        print(f"Los números que sí aparecen en la matriz son: {numeros_ordenados}")

# Programa principal
print("=== GENERADOR Y BUSCADOR DE MATRICES ===")

# Parte 1: Generar matriz
filas = int(input("Introduzca el número de filas: "))
columnas = int(input("Introduzca el número de columnas: "))

matriz = GenerarMatrizSimple(filas, columnas)
mostrar_matriz(matriz)

# Parte 2: Buscar y reemplazar
numero_a_buscar = int(input("\nIntroduce el número a buscar: "))
BuscarYReemplazar(matriz, numero_a_buscar)
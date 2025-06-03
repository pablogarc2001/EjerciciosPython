# Ejercicio de Matrices - Operaciones Básicas (1.5 puntos)
# (0.75 Parte 1) El usuario introducirá el número de filas y columnas que tendrán las matrices. Ambas matrices deben tener las mismas dimensiones para poder realizar operaciones entre ellas.
# Una vez que el usuario haya introducido las dimensiones, se llamará a la función CrearMatrices.

# Función CrearMatrices: Esta función recibirá como parámetros el número de filas y columnas que el usuario ha introducido.
# ○ Crear la primera matriz pidiendo al usuario que introduzca cada valor.
# ○ Crear la segunda matriz con números aleatorios entre 5 y 25.
# ○ Devolver ambas matrices.

# (0.75 Parte 2) El programa mostrará ambas matrices y luego pedirá al usuario que seleccione una operación:

# Opción 1: Sumar las dos matrices elemento por elemento
# Opción 2: Crear una nueva matriz donde cada elemento sea el mayor entre las dos matrices en esa posición
# Opción 3: Contar cuántos elementos de la primera matriz son mayores que los de la segunda matriz en la misma posición

# Se llamará a la función correspondiente según la opción elegida:

# Función SumarMatrices: Suma las dos matrices elemento por elemento y devuelve la matriz resultado.
# Función MatrizMaximos: Crea una nueva matriz tomando el elemento mayor de cada posición entre las dos matrices.
# Función ContarMayores: Compara elemento por elemento y cuenta cuántas veces los elementos de la primera matriz son mayores que los de la segunda.

# Nota: Mostrar las matrices originales y el resultado de la operación seleccionada con mensajes claros.


import random

filas = int(input("Introduzca el número de filas: "))
columnas = int(input("Introduzca el número de columnas: "))

def CrearMatrices(filas, columnas):
    # Crear primera matriz (input del usuario)
    matriz1 = []
    print(f"\nIntroduce los {filas * columnas} valores de la primera matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Introduce el valor para la posición ({i}, {j}): "))
            fila.append(valor)
        matriz1.append(fila)
    
    # Crear segunda matriz (aleatoria)
    matriz2 = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero_aleatorio = random.randint(5, 25)
            fila.append(numero_aleatorio)
        matriz2.append(fila)
    
    return matriz1, matriz2

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def SumarMatrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado

def MatrizMaximos(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            maximo = max(matriz1[i][j], matriz2[i][j])
            fila.append(maximo)
        resultado.append(fila)
    return resultado

def ContarMayores(matriz1, matriz2):
    contador = 0
    filas = len(matriz1)
    columnas = len(matriz1[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz1[i][j] > matriz2[i][j]:
                contador += 1
    return contador

# Crear ambas matrices
matriz1, matriz2 = CrearMatrices(filas, columnas)

print("\n" + "="*40)
print("MATRICES CREADAS")
print("="*40)
print("\nMatriz 1 (introducida por el usuario):")
mostrar_matriz(matriz1)
print("\nMatriz 2 (números aleatorios entre 5 y 25):")
mostrar_matriz(matriz2)

# Menú de opciones
print("\n" + "="*40)
print("SELECCIONA UNA OPERACIÓN")
print("="*40)
print("1. Sumar las dos matrices elemento por elemento")
print("2. Crear una matriz con los elementos máximos de cada posición")
print("3. Contar cuántos elementos de la matriz 1 son mayores que los de la matriz 2")

opcion = int(input("\nIntroduce tu opción (1, 2 o 3): "))

print("\n" + "="*40)
print("RESULTADO")
print("="*40)

if opcion == 1:
    matriz_suma = SumarMatrices(matriz1, matriz2)
    print("\nSuma de las matrices:")
    mostrar_matriz(matriz_suma)
    
elif opcion == 2:
    matriz_maximos = MatrizMaximos(matriz1, matriz2)
    print("\nMatriz con los elementos máximos de cada posición:")
    mostrar_matriz(matriz_maximos)
    
elif opcion == 3:
    cantidad_mayores = ContarMayores(matriz1, matriz2)
    print(f"\nCantidad de elementos de la matriz 1 que son mayores que los de la matriz 2: {cantidad_mayores}")
    
else:
    print("\nOpción no válida. Por favor, selecciona 1, 2 o 3.")
# Ejercicio de Matrices (1.5 puntos)
# (0.75 Parte 1) Inicialmente se pedirá al usuario el número de filas y columnas de una matriz (Se supone que los números introducidos son correctos).✔
# Una vez pedidos se llamará a la función GenerarMatriz.
# Función GenerarMatriz: Esta función recibirá como parámetros el número de filas y columnas que previamente se le han pedido al usuario. ○ Generar una matriz con números aleatorios entre 1 y 20.
#  Los números pueden repetirse en la matriz. ○ Devolver la matriz generada.✔
# 
# 
# 
# (0.75 Parte 2) Finalmente, se le estará pidiendo al usuario que elija una operación a realizar con la matriz:
# Opción 1: Mostrar solo la diagonal principal (el resto de elementos se ponen a 0)
# Opción 2: Calcular la suma de todos los elementos de la matriz
# Opción 3: Encontrar el número mayor y menor de la matriz
# Una vez que el usuario elija la opción, se llamará a la función correspondiente:
# Función MostrarDiagonal: Modifica la matriz original dejando solo los elementos de la diagonal principal, el resto se pone a 0.
# Función SumarElementos: Calcula y devuelve la suma total de todos los elementos de la matriz.
# Función EncontrarMaxMin: Encuentra y devuelve el valor máximo y mínimo de la matriz.



import random

def GenerarMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = random.randint(1, 20)
            fila.append(numero)
        matriz.append(fila)
    return matriz

def MostrarDiagonal(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if i != j: 
                matriz[i][j] = 0

def SumarElementos(matriz):
    suma_total = 0
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    return suma_total

def EncontrarMaxMin(matriz):
    maximo = matriz[0][0]
    minimo = matriz[0][0]
    
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
            if elemento < minimo:
                minimo = elemento
    
    return maximo, minimo

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# PROGRAMA PRINCIPAL
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

# Generar matriz
matriz = GenerarMatriz(filas, columnas)

print("\nMatriz original:")
mostrar_matriz(matriz)

# Menú de opciones
print("\nElige una opción:")
print("1. Mostrar solo diagonal principal")
print("2. Sumar todos los elementos")
print("3. Encontrar mayor y menor")

opcion = int(input("Opción: "))

if opcion == 1:
    MostrarDiagonal(matriz)
    print("\nMatriz con solo diagonal principal:")
    mostrar_matriz(matriz)
elif opcion == 2:
    suma = SumarElementos(matriz)
    print(f"\nLa suma total de elementos es: {suma}")
elif opcion == 3:
    mayor, menor = EncontrarMaxMin(matriz)
    print(f"\nNúmero mayor: {mayor}")
    print(f"Número menor: {menor}")
else:
    print("Opción no válida")

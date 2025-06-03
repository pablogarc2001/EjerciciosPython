# (0,75 puntos) Parte 1 – Generar la matriz
# Pide al usuario el número de filas y el número de columnas (se da por hecho que introduce valores válidos mayores que 0).

# Llama a la función GenerarMatriz con esos dos valores.
# GenerarMatriz(filas, columnas)
# Parámetros: números de filas y columnas introducidos.

# Crea y devuelve una matriz (lista de listas / array bidimensional) con números aleatorios entre 10 y 99 (ambos inclusive).
# Los números pueden repetirse.


# (0,75 puntos) Parte 2 – Operaciones sobre la matriz
# Después de mostrar la matriz generada, pregunta al usuario qué operación desea realizar y ejecuta la función correspondiente:

# Opción	Operación	Descripción	Función que se llama
# 1	Mostrar la matriz transpuesta	Intercambia filas por columnas (sin modificar la original) y la muestra por pantalla.	MostrarTranspuesta(matriz)
# 2	Calcular la suma de cada fila	Devuelve un vector donde cada posición contiene la suma de su fila correspondiente.	SumarFilas(matriz)
# 3	Contar pares / impares	Devuelve cuántos números pares y cuántos impares hay en total en la matriz.	ContarParesImpares(matriz)


import random

filas = int(input("Introduzca el número de filas: "))
columnas = int(input("Introduzca el número de columnas: "))

def GenerarMatrizAleatoria(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero_aleatorio = random.randint(10, 99)
            fila.append(numero_aleatorio)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    print("\nMatriz con números aleatorios del 1 al 100:")
    for fila in matriz:
        print(fila)

def mostrar_transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []

    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta

def sumar_filas(matriz):
    resultado = []
    for fila in matriz:
        resultado.append(sum(fila))
    return resultado


def contar_pares_impares(matriz):
    pares = 0
    impares = 0
    for fila in matriz:
        for n in fila:
            if n % 2  == 0:
                pares  += 1
            else:
                impares +=1
    return pares, impares


# Generamos la matriz
matriz = GenerarMatrizAleatoria(filas, columnas)
mostrar_matriz(matriz)

opcion=int(input("Qué  operación desea realizar? \n1.-Transponer Matriz \n2.-Sumar filas \n3.-Contar pares/impares\n "))


if opcion == 1:
    trans = mostrar_transpuesta(matriz)
    print("Transpuesta:")
    for fila in trans:
            print(fila)
elif opcion==2:
     sumas = sumar_filas(matriz)
     print("Suma de cada fila:", sumas)
elif opcion == 3:
    pares, impares = contar_pares_impares(matriz)
    print(f"Pares: {pares}  |  Impares: {impares}")

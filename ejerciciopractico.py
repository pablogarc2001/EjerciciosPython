import random

# Pedir dimensiones de la matriz
filas = int(input("Introduce el numero de filas: "))
columnas = int(input("Introduce el numero de columnas: "))

def GenerarMatriz(filas, columnas):
    total_casillas = filas * columnas
    lista_numeros = []
    
    for i in range(1, total_casillas):
        lista_numeros.append(i)
    
    cantidad_ceros = total_casillas - len(lista_numeros)
    for j in range(cantidad_ceros):
        lista_numeros.append(0)
    
    random.shuffle(lista_numeros)
    
    matriz = []
    indice = 0
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(lista_numeros[indice])
            indice += 1
        matriz.append(fila)
    return matriz

def SumarVecinos(matriz, fila, columna):
    # Inicializar la suma
    suma = 0
    
    # Dimensiones de la matriz
    filas_matriz = len(matriz)
    columnas_matriz = len(matriz[0])
    
    # Recorrer el área 3x3 alrededor de la posición (fila,columna)
    # Este bucle va desde fila-1 hasta fila+1 (o los límites de la matriz)
    for i in range(max(0, fila-1), min(filas_matriz, fila+2)):
        # Este bucle va desde columna-1 hasta columna+1 (o los límites de la matriz)
        for j in range(max(0, columna-1), min(columnas_matriz, columna+2)):
            # Sumar el valor de cada casilla del área
            suma += matriz[i][j]
    
    return suma

# Generar matriz
matriz = GenerarMatriz(filas, columnas)

# Imprimir las dimensiones y la matriz
print(f"Dimensiones de la matriz: {filas} filas x {columnas} columnas")
print("\nMatriz generada:")
for fila in matriz:
    print(fila)

# Pedir coordenadas directamente sin validación previa
print("\nIntroduce coordenadas para calcular la suma de vecinos:")
fila_usuario = int(input("Fila (0 a {}): ".format(filas-1)))
columna_usuario = int(input("Columna (0 a {}): ".format(columnas-1)))

# Verificar si las coordenadas están dentro del rango
if 0 <= fila_usuario < filas and 0 <= columna_usuario < columnas:
    # Calcular y mostrar la suma de vecinos
    suma = SumarVecinos(matriz, fila_usuario, columna_usuario)
    print(f"\nLa suma de la casilla ({fila_usuario}, {columna_usuario}) y sus vecinos es: {suma}")
else:
    print("Error: Las coordenadas introducidas están fuera del rango de la matriz.")
# Función para obtener las matrices recortada y sobrante
def obtener_recortes(matriz):
    if not matriz:
        return [], []
    
    num_filas = len(matriz)
    min_columnas = min(len(fila) for fila in matriz if fila)
    tam_recorte = min(num_filas, min_columnas)
    
    # Crear la matriz recortada (cuadrada)
    matriz_recorte = []
    for i in range(tam_recorte):
        fila_recorte = []
        for j in range(tam_recorte):
            fila_recorte.append(matriz[i][j])
        matriz_recorte.append(fila_recorte)
    
    # Crear la matriz sobrante
    matriz_sobrante = []
    
    # Agregar elementos sobrantes de las primeras tam_recorte filas
    for i in range(tam_recorte):
        if len(matriz[i]) > tam_recorte:
            fila_sobrante = matriz[i][tam_recorte:]
            matriz_sobrante.append(fila_sobrante)
    
    # Agregar filas completas sobrantes
    for i in range(tam_recorte, num_filas):
        matriz_sobrante.append(matriz[i])
    
    return matriz_recorte, matriz_sobrante

# Función para mostrar una matriz
def mostrar_matriz(matriz, tipo_matriz):
    print(f"\nMatriz {tipo_matriz}")
    print("-" * 20)
    if not matriz:
        print("Matriz vacía")
        return
    
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4}", end="")
        print()

# Programa principal
# Ejemplo del enunciado
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5],
    [6, 7],
    [8, 9, 10]
]

print("=== EJEMPLO DEL ENUNCIADO ===")
mostrar_matriz(matriz_ejemplo, "Original")

matriz_recorte, matriz_sobrante = obtener_recortes(matriz_ejemplo)

mostrar_matriz(matriz_recorte, "Recortada")
mostrar_matriz(matriz_sobrante, "Sobrante")

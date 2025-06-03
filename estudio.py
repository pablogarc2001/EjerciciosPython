# #1
# #MOSTRAR MATRIZ CON VALORES INTRODUCIDOS POR EL USUARIO SIN ALEATORIO

# #  # Pedimos al usuario el número de filas y columnas
# # filas = int(input("Introduce el número de filas: "))
# # columnas = int(input("Introduce el número de columnas: "))

# # def GenerarMatriz(filas, columnas):
# #     matriz = []

# #     print(f"\nIntroduce los {filas * columnas} valores de la matriz:")

# #     for i in range(filas):
# #         fila = []
# #         for j in range(columnas):
# #             valor = int(input(f"Introduce el valor para la posición ({i}, {j}): "))
# #             fila.append(valor)
# #         matriz.append(fila)

# #     return matriz

# # # Generamos la matriz y la guardamos
# # matriz = GenerarMatriz(filas, columnas)
 
# # # Mostramos la matriz final
# # print("\nMatriz generada:")
# # for fila in matriz:
# #     print(fila)

 


# #1.1
# #cREAR MATRIZ CON FILAS Y COLUMNAS ALEATORIAS
# import random

# # Rango para filas y columnas
# min_filas, max_filas = 2, 5
# min_columnas, max_columnas = 2, 5

# # Generamos filas y columnas aleatorias
# filas = random.randint(min_filas, max_filas)
# columnas = random.randint(min_columnas, max_columnas)

# print(f"Tamaño de las matrices: {filas} filas x {columnas} columnas\n")

# # Función para generar matriz aleatoria de tamaño filas x columnas con números entre 1 y 10
# # def generar_matriz_aleatoria(filas, columnas):
# #     matriz = []
# #     for _ in range(filas):
# #         fila = [random.randint(1, 10) for _ in range(columnas)]
# #         matriz.append(fila)
# #     return matriz

# # Si quiero que el usuario ingrese los numeros
# def generar_matriz_por_input(filas, columnas):
#     matriz = []  # inicializamos la matriz vacía
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Introduce el valor para la posición ({i}, {j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# # Función para mostrar matriz
# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Generamos dos matrices con el mismo tamaño, de forma aleatoria
# matriz1 = generar_matriz_por_input(filas,columnas)#generar_matriz_aleatoria(filas, columnas) 
# matriz2 = generar_matriz_por_input(filas,columnas)#generar_matriz_aleatoria (filas, columnas)

# print("Matriz 1:")
# mostrar_matriz(matriz1)
# print("\nMatriz 2:")
# mostrar_matriz(matriz2)

# Si quieres generar matrices con input del usuario, usa esto en su lugar:
# matriz1 = generar_matriz_por_input(filas, columnas)
# matriz2 = generar_matriz_por_input(filas, columnas)




# #2
# #PONER DE FORMA ALEATORIA SIN 0 SOBRANTES PIDIENDO LOS VALORES AL USUARIO
# # import random

# # # Pedimos al usuario el número de filas y columnas
# # filas = int(input("Introduce el número de filas: "))
# # columnas = int(input("Introduce el número de columnas: "))

# # def GenerarMatriz(filas, columnas):
# #     valores = []

# #     print(f"\nIntroduce los {filas * columnas} valores de la matriz:")

# #     for i in range(filas * columnas):
# #         valor = int(input(f"Introduce el valor {i + 1}: "))
# #         valores.append(valor)

# #     # Desordenamos los valores
# #     random.shuffle(valores)

# #     # Creamos la matriz con los valores aleatorios
# #     matriz = []
# #     index = 0
# #     for i in range(filas):
# #         fila = []
# #         for j in range(columnas):
# #             fila.append(valores[index])
# #             index += 1
# #         matriz.append(fila)

# #     return matriz

# # # Generamos la matriz y la guardamos
# # matriz = GenerarMatriz(filas, columnas)

# # # Mostramos la matriz final
# # print("\nMatriz con valores en orden aleatorio:")
# # for fila in matriz:
# #     print(fila)





# #3
# #ORDENAR SIN PEDIR NUMERO AL USUARIO Y SIN 0 SOBRANTES
# import random

# # # Puedes cambiar estos valores directamente en el código
# # filas = 3
# # columnas = 4

# # Pedimos al usuario el número de filas y columnas
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# def GenerarMatrizAleatoria(filas, columnas):
#     total_valores = filas * columnas

#     # Generamos los valores del 1 al total y los desordenamos
#     valores = list(range(1, total_valores + 1))
#     random.shuffle(valores)

#     # Creamos la matriz con los valores aleatorios
#     matriz = []
#     index = 0
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(valores[index])
#             index += 1
#         matriz.append(fila)

#     return matriz

# # Generamos la matriz
# matriz = GenerarMatrizAleatoria(filas, columnas)

# # Mostramos la matriz final
# print("\nMatriz generada aleatoriamente:")
# for fila in matriz:
#     print(fila)






# # #4
# # #RELLENR MATRIZ CON NÚMEROS ALEATORIOS DEL 1 AL 100 CON REPETIDOS POR EJEMPLO CAMBIA LUEGO LOS NUMEROS DEPENDIENDO DE LO QUE PIDAN 
# import random

# # # Pedimos al usuario el número de filas y columnas
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # filas = 3
# # columnas = 3

# def GenerarMatrizAleatoria(filas, columnas):
#     matriz = []
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             numero_aleatorio = random.randint(1, 100)
#             fila.append(numero_aleatorio)
#         matriz.append(fila)
#     return matriz

# # Generamos la matriz
# matriz = GenerarMatrizAleatoria(filas, columnas)

# # Mostramos la matriz final
# print("\nMatriz con números aleatorios del 1 al 100:")
# for fila in matriz:
#     print(fila)


#4.1
#RELLENAR MATRIZ CON NÚMEROS ALEATORIOS DEL 1 AL 100 SIN REPETIDOS POR EJEMPLO CAMBIA LUEGO LOS NUMEROS DEPENDIENDO DE LO QUE PIDAN 
# import random

# # Pedimos al usuario el número de filas y columnas
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))


# def GenerarMatrizSinRepetidos(filas, columnas):
#     # Verificar si es posible
#     total_celdas = filas * columnas
    
#     # Crear lista de números disponibles
#     numeros_disponibles = list(range(1, 101))  # del 1 al 100
#     random.shuffle(numeros_disponibles)  # mezclar
    
#     matriz = []
#     indice = 0
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(numeros_disponibles[indice])
#             indice += 1
#         matriz.append(fila)
#     return matriz

# # Generamos la matriz
# matriz = GenerarMatrizSinRepetidos(filas, columnas)

# # Mostramos la matriz final
# if matriz:
#     print("\nMatriz con números aleatorios del 1 al 100 (sin repetir):")
#     for fila in matriz:
#         print(fila)


# # #5
# # # MATRIZ DE PALABRAS INTRODUCIDAS POR EL USUARIO(LISTA)

# # # Pedimos al usuario el número de filas y columnas
# # filas = int(input("Introduce el número de filas: "))
# # columnas = int(input("Introduce el número de columnas: "))

# # def GenerarMatrizDePalabras(filas, columnas):
# #     matriz = []
# #     print(f"\nIntroduce {filas * columnas} palabras para llenar la matriz:")
# #     for i in range(filas):
# #         fila = []
# #         for j in range(columnas):
# #             palabra = input(f"Introduce la palabra para la posición ({i}, {j}): ")
# #             fila.append(palabra)
# #         matriz.append(fila)
# #     return matriz

# # # Generamos la matriz
# # matriz = GenerarMatrizDePalabras(filas, columnas)

# # # Mostramos la matriz final
# # print("\nMatriz de palabras:")
# # for fila in matriz:
# #     print(fila)



# #6
# ## MATRIZ DE PALABRAS USANDO DICCIONARIO

# # Pedimos al usuario el número de filas y columnas
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# def GenerarDiccionarioDePalabras(filas, columnas):
#     matriz = {}
#     print(f"\nIntroduce {filas * columnas} palabras para llenar la matriz CON DICCIONARIO:")

#     for i in range(filas):
#         for j in range(columnas):
#             palabra = input(f"Introduce la palabra para la posición ({i}, {j}): ")
#             matriz[(i, j)] = palabra

#     return matriz

# # Generamos el diccionario
# matriz = GenerarDiccionarioDePalabras(filas, columnas)

# # Mostramos la matriz formateada
# print("\nMatriz de palabras (usando diccionario):")
# for i in range(filas):
#     fila = []
#     for j in range(columnas):
#         fila.append(matriz[(i, j)])
#     print(fila)




# #7
# ## MATRIZ DE PALABRAS USANDO DICCIONARIO Y ORDEN ALEATORIO

# import random

# # Pedimos al usuario el número de filas y columnas
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# def GenerarDiccionarioDesordenado(filas, columnas):
#     total = filas * columnas
#     palabras = []

#     print(f"\nIntroduce {total} palabras para llenar la matriz:")

#     # Recogemos todas las palabras en una lista
#     for i in range(total):
#         palabra = input(f"Palabra {i + 1}: ")
#         palabras.append(palabra)

#     # Desordenamos la lista de palabras
#     random.shuffle(palabras)

#     # Creamos el diccionario con las posiciones y palabras aleatorias
#     matriz = {}
#     index = 0
#     for i in range(filas):
#         for j in range(columnas):
#             matriz[(i, j)] = palabras[index]
#             index += 1

#     return matriz

# # Generamos la matriz en diccionario
# matriz = GenerarDiccionarioDesordenado(filas, columnas)

# # Mostramos la matriz en forma de tabla
# print("\nMatriz de palabras desordenadas:")
# for i in range(filas):
#     fila = []
#     for j in range(columnas):
#         fila.append(matriz[(i, j)])
#     print(fila)


#8
# fila por fila

# filas = int(input("Filas: "))
# columnas = int(input("Columnas: "))
# matriz = []

# for i in range(filas):
#     fila = input(f"Introduce {columnas} palabras para la fila {i+1} separadas por espacios: ").split()
#     while len(fila) != columnas:
#         print("Número incorrecto de palabras. Intenta de nuevo.")
#         fila = input(f"Fila {i+1}: ").split()
#     matriz.append(fila)

# print(matriz)




#9
#SUMA DE MATRICES
# def leer_matriz(filas, columnas, nombre="matriz"):
#     matriz = []
#     print(f"\nIntroduce los valores de la {nombre}:")
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Elemento ({i},{j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# def sumar_matrices(m1, m2):
#     filas = len(m1)
#     columnas = len(m1[0])
#     resultado = []
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(m1[i][j] + m2[i][j])
#         resultado.append(fila)
#     return resultado

# # Entrada de dimensiones
# filas = int(input("Número de filas: "))
# columnas = int(input("Número de columnas: "))

# print("Matriz 1:")
# matriz1 = leer_matriz(filas, columnas, "matriz 1")
# print("Matriz 2:")
# matriz2 = leer_matriz(filas, columnas, "matriz 2")

# # Suma
# matriz_suma = sumar_matrices(matriz1, matriz2)

# # Mostrar resultado
# print("\nMatriz resultante de la suma:")
# for fila in matriz_suma:
#     print(fila)





#10
#SUMA DE MATRICES CON NUMEROS ALEATORIOS
# import random

# def generar_matriz_aleatoria(filas, columnas, minimo=1, maximo=100):
#     matriz = []
#     for _ in range(filas):
#         fila = [random.randint(minimo, maximo) for _ in range(columnas)]
#         matriz.append(fila)
#     return matriz

# def sumar_matrices(m1, m2):
#     filas = len(m1)
#     columnas = len(m1[0])
#     resultado = []
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(m1[i][j] + m2[i][j])
#         resultado.append(fila)
#     return resultado

# # Pedimos dimensiones
# filas = int(input("Número de filas: "))
# columnas = int(input("Número de columnas: "))

# # Generamos matrices aleatorias
# matriz1 = generar_matriz_aleatoria(filas, columnas)
# matriz2 = generar_matriz_aleatoria(filas, columnas)

# print("\nMatriz 1:")
# for fila in matriz1:
#     print(fila)

# print("\nMatriz 2:")
# for fila in matriz2:
#     print(fila)

# # Suma
# matriz_suma = sumar_matrices(matriz1, matriz2)

# print("\nMatriz resultado (suma):")
# for fila in matriz_suma:
#     print(fila)






#11
#PRODUCTO DE MATRICES
# def leer_matriz(filas, columnas, nombre="matriz"):
#     matriz = []
#     print(f"\nIntroduce los valores de la {nombre}:")
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Elemento ({i},{j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# def producto_matrices(m1, m2):
#     filas_m1 = len(m1)
#     columnas_m1 = len(m1[0])
#     filas_m2 = len(m2)
#     columnas_m2 = len(m2[0])
#     if columnas_m1 != filas_m2:
#         raise ValueError("No se pueden multiplicar matrices con esas dimensiones")

#     resultado = []
#     for i in range(filas_m1):
#         fila = []
#         for j in range(columnas_m2):
#             suma = 0
#             for k in range(columnas_m1):
#                 suma += m1[i][k] * m2[k][j]
#             fila.append(suma)
#         resultado.append(fila)
#     return resultado

# # Entrada dimensiones
# print("Dimensiones de la matriz 1:")
# filas1 = int(input("Número de filas: "))
# columnas1 = int(input("Número de columnas: "))

# print("Dimensiones de la matriz 2:")
# filas2 = int(input("Número de filas: "))
# columnas2 = int(input("Número de columnas: "))

# # Comprobación rápida antes de pedir valores
# if columnas1 != filas2:
#     print("Error: El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2.")
#     exit()

# # Leer matrices
# matriz1 = leer_matriz(filas1, columnas1, "matriz 1")
# matriz2 = leer_matriz(filas2, columnas2, "matriz 2")

# # Producto
# matriz_producto = producto_matrices(matriz1, matriz2)

# # Mostrar resultado
# print("\nMatriz resultante del producto:")
# for fila in matriz_producto:
#     print(fila)




#12
#PRODUCTO DE MATRICES CON NUMEROS ALEATORIOS
# import random

# def generar_matriz_aleatoria(filas, columnas, minimo=1, maximo=100):
#     matriz = []
#     for _ in range(filas):
#         fila = [random.randint(minimo, maximo) for _ in range(columnas)]
#         matriz.append(fila)
#     return matriz

# def producto_matrices(m1, m2):
#     filas_m1 = len(m1)
#     columnas_m1 = len(m1[0])
#     filas_m2 = len(m2)
#     columnas_m2 = len(m2[0])
    
#     if columnas_m1 != filas_m2:
#         raise ValueError("No se pueden multiplicar matrices con esas dimensiones")

#     resultado = []
#     for i in range(filas_m1):
#         fila = []
#         for j in range(columnas_m2):
#             suma = 0
#             for k in range(columnas_m1):
#                 suma += m1[i][k] * m2[k][j]
#             fila.append(suma)
#         resultado.append(fila)
#     return resultado

# # Pedimos dimensiones
# print("Dimensiones de matriz 1:")
# filas1 = int(input("Número de filas: "))
# columnas1 = int(input("Número de columnas: "))

# print("Dimensiones de matriz 2:")
# filas2 = int(input("Número de filas: "))
# columnas2 = int(input("Número de columnas: "))

# # Validamos dimensiones para multiplicar
# if columnas1 != filas2:
#     print("Error: columnas de matriz 1 deben ser iguales a filas de matriz 2")
#     exit()

# # Generamos matrices aleatorias
# matriz1 = generar_matriz_aleatoria(filas1, columnas1)
# matriz2 = generar_matriz_aleatoria(filas2, columnas2)

# print("\nMatriz 1:")
# for fila in matriz1:
#     print(fila)

# print("\nMatriz 2:")
# for fila in matriz2:
#     print(fila)

# # Producto
# matriz_producto = producto_matrices(matriz1, matriz2)

# print("\nMatriz resultado (producto):")
# for fila in matriz_producto:
#     print(fila)






#13
#Suma de matrices con matrices aleatorias desordenadas sin ceros sobrantes
# import random

# Pedimos dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# def GenerarMatrizAleatoria(filas, columnas):
#     total_valores = filas * columnas
#     valores = list(range(1, total_valores + 1))
#     random.shuffle(valores)
#     matriz = []
#     index = 0
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(valores[index])
#             index += 1
#         matriz.append(fila)
#     return matriz

# def sumar_matrices(m1, m2):
#     filas = len(m1)
#     columnas = len(m1[0])
#     resultado = []
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(m1[i][j] + m2[i][j])
#         resultado.append(fila)
#     return resultado

# matriz1 = GenerarMatrizAleatoria(filas, columnas)
# matriz2 = GenerarMatrizAleatoria(filas, columnas)

# print("\nMatriz 1:")
# for fila in matriz1:
#     print(fila)

# print("\nMatriz 2:")
# for fila in matriz2:
#     print(fila)

# suma = sumar_matrices(matriz1, matriz2)

# print("\nMatriz suma:")
# for fila in suma:
#     print(fila)





#14
#Producto de matrices con matrices aleatorias desordenadas sin ceros sobrantes
# import random

# # Pedimos dimensiones (asegúrate que columnas1 == filas2)
# filas1 = int(input("Introduce el número de filas de la matriz 1: "))
# columnas1 = int(input("Introduce el número de columnas de la matriz 1: "))

# filas2 = columnas1  # obligatorio para multiplicar
# columnas2 = int(input(f"Introduce el número de columnas de la matriz 2 (filas = {filas2}): "))

# def GenerarMatrizAleatoria(filas, columnas):
#     total_valores = filas * columnas
#     valores = list(range(1, total_valores + 1))
#     random.shuffle(valores)
#     matriz = []
#     index = 0
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(valores[index])
#             index += 1
#         matriz.append(fila)
#     return matriz

# def multiplicar_matrices(m1, m2):
#     filas_m1 = len(m1)
#     columnas_m1 = len(m1[0])
#     columnas_m2 = len(m2[0])
#     resultado = []
#     for i in range(filas_m1):
#         fila = []
#         for j in range(columnas_m2):
#             suma = 0
#             for k in range(columnas_m1):
#                 suma += m1[i][k] * m2[k][j]
#             fila.append(suma)
#         resultado.append(fila)
#     return resultado

# matriz1 = GenerarMatrizAleatoria(filas1, columnas1)
# matriz2 = GenerarMatrizAleatoria(filas2, columnas2)

# print("\nMatriz 1:")
# for fila in matriz1:
#     print(fila)

# print("\nMatriz 2:")
# for fila in matriz2:
#     print(fila)

# producto = multiplicar_matrices(matriz1, matriz2)

# print("\nMatriz producto:")
# for fila in producto:
#     print(fila)





#15
#Generar matriz diagonal (solo elementos en diagonal principal, resto ceros)

# def generar_matriz_diagonal(filas, columnas):
#     matriz = []
#     print(f"Introduce los valores para la diagonal principal (hasta {min(filas, columnas)} elementos):")
#     diagonal = []
#     for i in range(min(filas, columnas)):
#         valor = int(input(f"Valor para la posición ({i},{i}): "))
#         diagonal.append(valor)
    
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             if i == j:
#                 fila.append(diagonal[i])  # Elemento en la diagonal
#             else:
#                 fila.append(0)  # Fuera de la diagonal es 0
#         matriz.append(fila)
#     return matriz

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Pedimos al usuario dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # Generamos la matriz diagonal
# matriz_diagonal = generar_matriz_diagonal(filas, columnas)

# # Mostramos la matriz
# print("\nMatriz diagonal generada:")
# mostrar_matriz(matriz_diagonal)




#16
#Matriz con diagonal secundaria (de la esquina superior derecha a la esquina inferior izquierda)
# def generar_matriz_diagonal_secundaria(filas, columnas):
#     matriz = []
#     print(f"Introduce los valores para la diagonal secundaria (hasta {min(filas, columnas)} elementos):")
#     diagonal_sec = []
#     for i in range(min(filas, columnas)):
#         valor = int(input(f"Valor para la posición ({i},{columnas - 1 - i}): "))
#         diagonal_sec.append(valor)
    
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             # Comprobamos si está en la diagonal secundaria
#             if j == columnas - 1 - i:
#                 fila.append(diagonal_sec[i])
#             else:
#                 fila.append(0)
#         matriz.append(fila)
#     return matriz

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Pedimos al usuario dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # Generamos la matriz con diagonal secundaria
# matriz_diagonal_sec = generar_matriz_diagonal_secundaria(filas, columnas)

# # Mostramos la matriz
# print("\nMatriz con diagonal secundaria generada:")
# mostrar_matriz(matriz_diagonal_sec)




#17
# #crear matriz entera y luego mostrar diagonal principal  con 0
# def crear_matriz(filas, columnas):
#     matriz = []
#     print(f"Introduce los valores para una matriz de {filas}x{columnas}:")
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Elemento ({i},{j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# def poner_diagonal_principal_a_cero(matriz):
#     filas = len(matriz)
#     columnas = len(matriz[0]) if filas > 0 else 0
#     for i in range(min(filas, columnas)):
#         matriz[i][i] = 0

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Pedir dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # Crear matriz
# matriz = crear_matriz(filas, columnas)

# # Mostrar matriz original antes de modificar
# print("\nMatriz original:")
# mostrar_matriz(matriz)

# # Modificar diagonal principal a 0
# poner_diagonal_principal_a_cero(matriz)

# # Mostrar matriz resultante
# print("\nMatriz con diagonal principal en 0:")
# mostrar_matriz(matriz)




#18
#crear matriz entera y luego mostrar diagonal principal  
# def crear_matriz(filas, columnas):
#     matriz = []
#     print(f"Introduce los valores para una matriz de {filas}x{columnas}:")
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Elemento ({i},{j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# def dejar_solo_diagonal_principal(matriz):
#     filas = len(matriz)
#     columnas = len(matriz[0])
#     for i in range(filas):
#         for j in range(columnas):
#             if i != j:
#                 matriz[i][j] = 0

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Pedir dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # Crear matriz
# matriz = crear_matriz(filas, columnas)

# # Mostrar matriz original antes de modificar
# print("\nMatriz original:")
# mostrar_matriz(matriz)

# # Dejar solo diagonal principal, resto 0
# dejar_solo_diagonal_principal(matriz)

# # Mostrar matriz resultante
# print("\nMatriz con solo la diagonal principal conservada:")
# mostrar_matriz(matriz)




# #19
# #crear matriz entera y luego mostrar diagonal secundaria  
# def crear_matriz(filas, columnas):
#     matriz = []
#     print(f"Introduce los valores para una matriz de {filas}x{columnas}:")
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Elemento ({i},{j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# def dejar_solo_diagonal_secundaria(matriz):
#     filas = len(matriz)
#     columnas = len(matriz[0]) if filas > 0 else 0
#     for i in range(filas):
#         for j in range(columnas):
#             # Condición para la diagonal secundaria: j == columnas - 1 - i
#             if j != columnas - 1 - i:
#                 matriz[i][j] = 0

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Pedir dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # Crear matriz
# matriz = crear_matriz(filas, columnas)

# # Mostrar matriz completa antes de modificar
# print("\nMatriz original:")
# mostrar_matriz(matriz)

# # Dejar solo diagonal secundaria, resto 0
# dejar_solo_diagonal_secundaria(matriz)

# # Mostrar matriz resultante
# print("\nMatriz con solo la diagonal secundaria conservada:")
# mostrar_matriz(matriz)




# #20
# #crear matriz entera y luego mostrar diagonal secundaria  con 0
# def crear_matriz(filas, columnas):
#     matriz = []
#     print(f"Introduce los valores para una matriz de {filas}x{columnas}:")
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             valor = int(input(f"Elemento ({i},{j}): "))
#             fila.append(valor)
#         matriz.append(fila)
#     return matriz

# def poner_cero_diagonal_secundaria(matriz):
#     filas = len(matriz)
#     columnas = len(matriz[0]) if filas > 0 else 0
#     for i in range(filas):
#         for j in range(columnas):
#             if j == columnas - 1 - i:  # diagonal secundaria
#                 matriz[i][j] = 0

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         print(fila)

# # Pedir dimensiones
# filas = int(input("Introduce el número de filas: "))
# columnas = int(input("Introduce el número de columnas: "))

# # Crear matriz
# matriz = crear_matriz(filas, columnas)

# # Mostrar matriz completa antes de modificar
# print("\nMatriz original:")
# mostrar_matriz(matriz)

# # Poner a 0 la diagonal secundaria
# poner_cero_diagonal_secundaria(matriz)

# # Mostrar matriz resultante
# print("\nMatriz con la diagonal secundaria puesta a 0:")
# mostrar_matriz(matriz)

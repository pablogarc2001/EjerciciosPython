class MatrizRecortes:
    def __init__(self, matriz):
        self.matriz = matriz

    def Recortes(self):
        # Calculamos número de filas y columnas
        num_filas = len(self.matriz)
        num_columnas = max(len(fila) for fila in self.matriz)  # Obtenemos el máximo número de columnas
        
        # Encontramos el tamaño mínimo entre filas y columnas
        tam_recorte = min(num_filas, num_columnas)
        
        # Creamos la matriz recortada (cuadrada)
        matriz_recorte = []
        for i in range(tam_recorte):
            fila_recorte = []
            for j in range(tam_recorte):
                # Asegurarnos de que no accedemos a índices fuera de rango
                if j < len(self.matriz[i]):
                    fila_recorte.append(self.matriz[i][j])
            if fila_recorte:
                matriz_recorte.append(fila_recorte)
        
        # Creamos la matriz sobrante
        matriz_sobrante = []
        
        # Si hay más columnas que filas, agregamos los elementos restantes por fila
        if num_columnas > tam_recorte:
            for i in range(tam_recorte):
                fila_sobrante = []
                for j in range(tam_recorte, len(self.matriz[i])):
                    fila_sobrante.append(self.matriz[i][j])
                if fila_sobrante:  # Solo agregamos si la fila no está vacía
                    matriz_sobrante.append(fila_sobrante)
        
        # Si hay más filas que columnas, agregamos las filas restantes completas
        if num_filas > tam_recorte:
            for i in range(tam_recorte, num_filas):
                matriz_sobrante.append(self.matriz[i])
        
        return (matriz_recorte, matriz_sobrante)

    def MostrarMatriz(self, matriz, tipo_matriz):
        print(f"\nMatriz {tipo_matriz}")
        print("-" * 20)
        
        for fila in matriz:
            for elemento in fila:
                print(f"{elemento:4}", end="")
            print()

def main():
    # Ejemplo de matriz
    matriz_ejemplo = [
        [1, 2, 3],
        [4, 5],
        [6, 7],
        [8, 9, 10]
    ]
    
    # Instanciamos la clase con la matriz
    recortes = MatrizRecortes(matriz_ejemplo)
    
    # Mostrar matriz original
    recortes.MostrarMatriz(matriz_ejemplo, "Original")
    
    # Obtener recortes
    matriz_recorte, matriz_sobrante = recortes.Recortes()
    
    # Mostrar resultados
    recortes.MostrarMatriz(matriz_recorte, "Recortada")
    recortes.MostrarMatriz(matriz_sobrante, "Sobrante")

if __name__ == "__main__":
    main()

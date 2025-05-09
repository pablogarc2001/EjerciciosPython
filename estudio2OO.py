# crear diccionario de palabras que tenga distintas traducciones

class Diccionario:
    def __init__(self, nombre="Anaya"):
        self.NombreDic = nombre
        self.DPalabras = dict()  # diccionario vacío
        self.__idiomas= {"Inglés": 0, "Francés": 1, "Alemán": 2}  # idiomas y su posición en la lista de traducciones
        
    def Introducir_Palabras(self, P):
        resultado=""
        if P in self.DPalabras:
            resultado= "Ya existe"
        else:
            self.DPalabras[P] = ["","",""]
            resultado = "Insertada"
        return resultado  
          
    def Introducir_Traduccion(self, P,Idioma, Trad):
        if P in self.DPalabras:
            self.DPalabras[P][self.__idiomas[Idioma]]=Trad
            resultado = "Introducido"
            return resultado
        else:
            resultado = "Error, palabra no introducida"
    def Mostrar_Traduccion(self):
        pass
    def Traducciones_Idioma(self):
        pass
    def Mostrar_Diccionario(self):
        pass
    def __str__(self):
        resultado = self.NombreDic +"\n\n"
        for p in self.DPalabras:
            resultado += p + "\n"
            for i in self.__idiomas:
                if self.DPalabras[p][self.__idiomas[i]] != "":
                    resultado += "\t" + self.DPalabras[p][self.__idiomas[i]] + "\n"

        return resultado

#####################
#####################
MiDiccionario = Diccionario()  # Crear una única instancia fuera del bucle
opcion = -1  # Inicializar con un valor distinto de 0

while opcion != 0:
    print("\n--- MENÚ ---")
    print("0.- Salir")
    print("1.- Introducir palabra")
    print("2.- Introducir traducción")
    print("3.- Mostrar traducción ")
    print("4.- Mostrar traducciones idioma")  # bucle
    print("5.- Mostrar diccionario")

    opcion = int(input("Introduzca una opción: "))

    if opcion == 1:
        palabra = input("Palabra: ")
        print(MiDiccionario.Introducir_Palabras(palabra))
    elif opcion == 2:
        palabra = input("Palabra: ")
        idioma = input("Idioma (Inglés, Francés, Alemán): ")
        traduccion = input("Traducción: ")
        print(MiDiccionario.Introducir_Traduccion(palabra, idioma, traduccion))
    elif opcion == 3:
        pass  
    elif opcion == 4:
        pass  
    elif opcion == 5:
        print(MiDiccionario)
    elif opcion == 0:
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")


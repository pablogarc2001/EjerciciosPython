class alumno:
    #ESTO ES UNA PRUEBA GIT
    def __init__(self, nombre, edad = 18):
        self.nombre = nombre
        self.edad = edad
        

class aula:
    def __init__(self, ciclo = "DAM", curso = 1):
        self.ciclo = ciclo
        self.curso = curso
        self.listadoAlumnos = list()
        
    def insertarAlumnos(self,alumno):
        if len(self.listadoAlumnos) < 30:
            self.listadoAlumnos.append(alumno)
            return "Correcto"
        else:
            return "Aula llena"
        
    def __str__(self):
        
        lista_nombres = list()
        for a in self.listadoAlumnos:
            lista_nombres.append(a.nombre)
        
        resultado = "Ciclo: {} ,".format(self.ciclo)
        resultado += "Curso: {} ,".format(self.curso)
        resultado += "Alumnos: {} ".format(lista_nombres)
        
        return resultado
    
    def ExisteAlumno(self,nombre):
        lista_nombres = list()
        for a in self.listadoAlumnos:
            lista_nombres.append(a.nombre)
            
        if nombre in lista_nombres:
            return True
        else:
            return False
    
    def AlumnosMenores(self):  
        rango_edades = {"menores": []}
        for alumno in self.listadoAlumnos:
            edad = alumno.edad
            if edad >= 18:
                if edad in rango_edades:
                    rango_edades[edad].append(alumno.nombre)
                else:
                    rango_edad = edad//10
                    rango_edades[rango_edad] = []
                    rango_edades[rango_edad].append(alumno.nombre)
            else:
                rango_edades["menores"].append(alumno.nombre)
        
        return rango_edades
                
                


def main():
    
    print("1.-Crear Alumno\n2.-Crear Aula \n3.-Insertar Alumno Aula \n4.- Mostrar todos \n5.-Existe Alumno \n6.-Inserta Alumnos Aula no repetidos \n7.-Alumnos menores \n8.-Salir\n")
    opcion = int(input("Seleccione una opción: "))
    
    while opcion != 8:
        if opcion == 1:
            N = input("Teclee un nombre ")
            E = int(input("Teclee una edad "))
            A = alumno(N,E)
        if opcion == 2:
            Ciclo = input("Teclee un nombre para el ciclo ")
            Curso = int(input("Teclee el curso "))
            nueva_aula = aula(Ciclo,Curso)
        if opcion == 3: #Se debe de haber creado previamente un alumno
            nueva_aula.insertarAlumnos(A)
        if opcion == 4:
            print(nueva_aula)
        if opcion == 5:
            nombre_buscar = input("Teclee un nombre ")
            comprobacion = nueva_aula.ExisteAlumno(nombre_buscar)
            if comprobacion == True:
                print("Si existe un alumno con el nombre {}".format(nombre_buscar))
            else:
                print("No existe un alumno con el nombre {}".format(nombre_buscar))
                
        if opcion == 6:
            
            nombre_nuevo_alumno = input("Teclee un nombre ")
            edad_nuevo_alumno = int(input("Teclee una edad "))
            comprobacion = nueva_aula.ExisteAlumno(nombre_nuevo_alumno)
            if comprobacion == True:
                print("Ya existe un alumno con el nombre {}".format(nombre_buscar))
            else:
                nuevo_alumno = alumno(nombre_nuevo_alumno,edad_nuevo_alumno)
                nueva_aula.insertarAlumnos(nuevo_alumno)
                
        if opcion == 7:
           print(nueva_aula.AlumnosMenores())
           
        print("1.- Crear Alumno \n2.-Crear Aula \n3.-Insertar Alumno Aula \n4.- Mostrar todos \n5.- Existe Alumno \n6.-Inserta Alumnos Aula no repetidos \n7.-Alumnos menores \n8.-Salir \n")
        opcion = int(input("Seleccione una opción: "))
        
if __name__ == "__main__":
    main()           


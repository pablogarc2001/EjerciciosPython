import random


class Examen:
    def __init__(self, tema):
        self.tema = tema
        self.Preguntas = dict()

    def InsertarPregunta(self, pregunta, respuesta, puntuacion, tema='Python'):
        # Comprobaciones de puntuacion
        if puntuacion < 0:
            puntuacion = 0
        elif puntuacion > 10:
            puntuacion = 10

     # Obtener la lista de preguntas del tema especificado
    # Si el tema no existe en el diccionario, se devuelve una lista vacía []
        preguntas_tema = self.Preguntas.get(tema, [])
        preguntas_tema.append((pregunta, respuesta, puntuacion))
        self.Preguntas[tema] = preguntas_tema

    def __str__(self):
        cadena = ''
        # Por cada tema
        for tema, preguntas in self.Preguntas.items():
            cadena += f'\nTema: {tema}'

            # Por cada pregunta
            for pregunta in preguntas:
                cadena += f'\n\tPregunta: {pregunta[0]}\n\tRespuesta: {pregunta[1]}\n\tPuntuacion: {pregunta[2]}\n'
        return cadena

    def GenerarExamen(self, tema, numero_preguntas):
    # Verifica si el tema tiene suficientes preguntas para generar el examen
        if len(self.Preguntas.get(tema, [])) >= numero_preguntas:

            preguntas_respondidas = []  # Lista para almacenar las preguntas ya usadas
            puntuacion = 0  # Contador de la puntuación obtenida
            puntacion_maxima = 0  # Puntuación máxima posible en el examen

            # Mientras no se hayan respondido todas las preguntas solicitadas
            while len(preguntas_respondidas) < numero_preguntas:
                # Selecciona una pregunta aleatoria del tema
                numero_aleatorio = random.randint(0, len(self.Preguntas[tema]) - 1)
                pregunta = self.Preguntas[tema][numero_aleatorio]

                # Verifica que la pregunta no se repita en el examen
                if pregunta not in preguntas_respondidas:
                    # Solicita al usuario la respuesta y la compara con la correcta
                    if input(f'{pregunta[0]}: ') == str(pregunta[1]):
                        puntuacion += pregunta[2]  # Suma la puntuación si es correcta
                    
                    # Aumenta la puntuación máxima en función de la pregunta actual
                    puntacion_maxima += pregunta[2]

                    # Agrega la pregunta a la lista de preguntas respondidas
                    preguntas_respondidas.append(pregunta)

            # Muestra los resultados finales del examen
            print(f'Total preguntas: {numero_preguntas}\nPuntuacion maxima posible: {puntacion_maxima}\nPuntuacion obtenida: {puntuacion}')

        else:
            # Si no hay suficientes preguntas en el tema, muestra un mensaje de error
            print('El tema no existe o no tiene suficientes preguntas')

opciones = "\n1.-Crear Examen\n2.-Introducir Pregunta\n3.-Imprimir preguntas\n4.-Generar Examen\n5.-Salir\n"
examen = None
o = int(input(opciones))
while o != 5:
    if o == 1:
        nombre_modulo = input('Introduce el nombre del modulo: ')
        examen = Examen(nombre_modulo)
    elif o == 2:
        if examen is not None:
            tema = input('Introduce el Tema de la pregunta (ENTER para por defecto): ')
            pregunta = input('Introduce la pregunta: ')
            respuesta = input('Introduce la respuesta: ')
            puntuacion = int(input('Introduce la puntuacion de la pregunta: '))

            if tema != '':
                examen.InsertarPregunta(pregunta, respuesta, puntuacion, tema)
            else:  # Si el tema esta vacio usamos el otro constructor
                examen.InsertarPregunta(pregunta, respuesta, puntuacion)
        else:
            print('Debe crear un examen primero')
    elif o == 3:
        if examen is not None:
            print(examen)
        else:
            print('Debe crear un examen primero')
    elif o == 4:
        tema = str(input('Introduce el Tema del examen: '))
        numero_preguntas = int(input('Introduce el numero de preguntas: '))
        examen.GenerarExamen(tema, numero_preguntas)
    elif o==5:
        exit

    o = int(input(opciones))

print("Sesion finalizada.")
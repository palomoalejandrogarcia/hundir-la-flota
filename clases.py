import numpy as np
from variables import *

class Tablero:
    """Crea el tablero asociado al jugador.

    Attributes:
        id_jugador (str): Identificador del jugador.
    """
    def __init__(self, id_jugador):
        """Constructor que inicia el tablero del jugador.

        Args:
            id_jugador: El id del jugador.
        """
        self.id_jugador = id_jugador
        # Inicializamos la matriz del tablero con el símbolo de agua
        self.tablero = np.full((TAMANO_TABLERO, TAMANO_TABLERO), SIMBOLOS["agua"])
        self.disparos = np.full((TAMANO_TABLERO, TAMANO_TABLERO), SIMBOLOS["agua"])
        # Lista que guardará las coordenadas de los barcos
        self.barcos = []

    def colocar_barcos(self):
        """Función para colocar barcos de forma aleatoria"""
        direccion = [(0, 1), (0, -1), (1, 0), (-1, 0)] # las cuatro direcciones a las que podemos seguir pintando el barco
        coordenadas_ocupadas = set()

        for i in ESLORAS:
            colocado = False # variable para saber si el barco encaja y no se sale o solapa con otro barco
            # Repetimos el intento hasta encontrar una posición válida para el barco
            while not colocado:
                vector_direccion = np.array(direccion[np.random.randint(0, 4)]) # elegimos una dirección
                inicio = np.random.randint(0, TAMANO_TABLERO, size=2) # elegimos una coordenada donde empezar a pintar
                
                barco = [] # la variable contiene las coordenadas que ocupa el barco
                valido = True

                for j in range(i):
                    if j == 0:
                        coord = inicio
                    else:
                        coord = barco[j-1] + vector_direccion

                    # Validamos que la coordenada no se salga del tablero
                    if not (0 <= coord[0] < TAMANO_TABLERO and 0 <= coord[1] < TAMANO_TABLERO):
                        valido = False
                        break
                    
                    #Validamos que la casilla no esté ocupada por otro barco
                    coord_tupla = tuple(coord)
                    if coord_tupla in coordenadas_ocupadas:
                        valido = False
                        break
                    barco.append(coord)
                # si todas las casillas son validas
                if valido:
                        barco_final = [np.array(coord) for coord in barco]
                        self.barcos.append(barco_final)
                        
                        for coord in barco:
                            c_tuple = tuple(coord)
                            coordenadas_ocupadas.add(c_tuple)
                            self.tablero[c_tuple[0], c_tuple[1]] = SIMBOLOS["barco"]
                            
                        colocado = True

    def mostrar(self):
        """Imprime el tablero en la consola"""
        for fila in self.tablero:
            print(fila)
        print('\n')
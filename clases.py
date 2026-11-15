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
        direccion = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in ESLORAS:
            vector_direccion = np.array(direccion[np.random.randint(0, 4)])
            inicio = np.random.randint(0, TAMANO_TABLERO, size=2)
            
            barco = []
            for j in range(i):
                if j == 0:
                    coord = inicio
                else:
                    coord = barco[j-1] + vector_direccion
                barco.append(coord)
            
            barco_final = [np.array(coord) for coord in barco]
            self.barcos.append(barco_final)
            
            for coord in barco:
                self.tablero[coord[0], coord[1]] = SIMBOLOS["barco"]

    def mostrar(self):
        """Imprime el tablero en la consola"""
        for fila in self.tablero:
            print(fila)
        print('\n')


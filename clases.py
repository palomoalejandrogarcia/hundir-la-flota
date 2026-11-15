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
        self.disparos = np.array((TAMANO_TABLERO, TAMANO_TABLERO))
        # Lista que guardará las coordenadas de los barcos
        self.barcos = []
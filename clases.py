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
        self.tablero = np.full(
            (TAMANO_TABLERO, TAMANO_TABLERO),
            SIMBOLOS["agua"])
        self.disparos = np.full(
            (TAMANO_TABLERO, TAMANO_TABLERO),
            SIMBOLOS["agua"])
        # Lista que guardará las coordenadas de los barcos
        self.barcos = []

    def colocar_barcos(self):
        """Función para colocar barcos de forma aleatoria."""
        direccion = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)]  # las cuatro direcciones a las que podemos seguir pintando el barco
        coordenadas_ocupadas = set()

        esloras_partida = []
        for cantidad, eslora in zip(BARCOS, ESLORAS):
            esloras_partida.extend([eslora] * cantidad)

        for i in sorted(esloras_partida, reverse=True):
            # variable para saber si el barco encaja y no se sale o solapa con otro barco
            colocado = False
            # Repetimos el intento hasta encontrar una posición válida para el barco
            while not colocado:
                vector_direccion = np.array(
                    direccion[np.random.randint(0, 4)])  # elegimos una dirección
                # elegimos una coordenada (fila, columna) donde empezar a pintar
                inicio = np.random.randint(0, TAMANO_TABLERO, size=2)

                barco = []  # la variable contiene las coordenadas que ocupa el barco
                valido = True

                for j in range(i):
                    if j == 0:
                        coord = inicio
                    else:
                        coord = barco[j-1] + vector_direccion

                    # Validamos que la coordenada no se salga del tablero
                    if not (
                            0 <= coord[0] < TAMANO_TABLERO and 0 <= coord[1] <
                            TAMANO_TABLERO):
                        valido = False
                        break

                    # Validamos que la casilla no esté ocupada por otro barco
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
                        fila, columna = int(coord[0]), int(coord[1])
                        self.tablero[fila, columna] = SIMBOLOS["barco"]

                        # Añadimos la casilla del barco y las casillas colindantes
                        for desplazamiento_fila in (-1, 0, 1):
                            for desplazamiento_col in (-1, 0, 1):
                                nueva_fila, nueva_col = fila + desplazamiento_fila, columna + desplazamiento_col
                                # Este if se asegura que no entren las coordenadas colindantes de un barco si estan fuera del tablero
                                if 0 <= nueva_fila < TAMANO_TABLERO and 0 <= nueva_col < TAMANO_TABLERO:
                                    coordenadas_ocupadas.add((nueva_fila, nueva_col))

                    colocado = True

    def mostrar(self):
        """Imprime el tablero en la consola."""
        for fila in self.tablero:
            print(fila)
        print('\n')

    def recibir_disparo(self, columna, fila):
        """Dada la columna (eje horizontal) y fila (eje vertical) de la coordenada,
        retorna si el disparo dio en el agua, un trozo del barco, si lo hundió
        o si el disparo se repitió.

        Args:
            columna (int): Coordenada horizontal (eje X), de 0 a TAMANO_TABLERO - 1.
            fila (int): Coordenada vertical (eje Y), de 0 a TAMANO_TABLERO - 1.

        Returns:
            str: Posibles resultados del disparo: agua, tocado, tocado y hundido,
                repetido o fuera de rango.
        """
        # Validamos que la coordenada esté dentro del tablero
        if not (
                columna in range(0, TAMANO_TABLERO) and
                fila in range(0, TAMANO_TABLERO)):
            return MENSAJES_FIJOS["fuera"]

        # Internamente indexamos la matriz como [fila, columna]
        casilla_actual = self.tablero[fila, columna]

        # Comprobamos si ya se había disparado en esa casilla
        if casilla_actual in (SIMBOLOS["tocado"], SIMBOLOS["fallo"]):
            return MENSAJES_FIJOS["repetido"]

        # Comprobamos si hay un barco en esa casilla
        if casilla_actual == SIMBOLOS["barco"]:
            # Actualizamos tanto el tablero del jugador como el tablero de disparos que ve el enemigo
            self.tablero[fila, columna] = SIMBOLOS["tocado"]
            self.disparos[fila, columna] = SIMBOLOS["tocado"]
            for barco in self.barcos:
                # Buscamos el barco que ocupa esa casilla (guardada como [fila, columna])
                if any(
                        casilla[0] == fila and casilla[1] == columna
                        for casilla in barco):
                    # Devolvemos hundido solo si TODAS las casillas del barco están tocadas
                    if all(
                            self.tablero[casilla[0],
                                         casilla[1]] == SIMBOLOS["tocado"]
                            for casilla in barco):
                        return MENSAJES_FIJOS["hundido"]
            return MENSAJES_FIJOS["tocado"]

        # Si hemos llegado aquí entonces en la casilla había agua
        self.tablero[fila, columna] = SIMBOLOS["fallo"]
        self.disparos[fila, columna] = SIMBOLOS["fallo"]
        return MENSAJES_FIJOS["agua"]

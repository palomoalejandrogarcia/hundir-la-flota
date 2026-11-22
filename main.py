#Preparar la partida: crear los dos tableros (el tuyo y el de la máquina) y colocar los barcos de ambos.
#Bucle principal: empieza el jugador y los turnos se alternan.
#Turno del jugador: pedir coordenada, validarla, disparar y mostrar el resultado.
#Regla de repetir turno: si aciertas, vuelves a disparar; si es agua, pasa el turno. Esto vale también para la máquina.
#Turno de la máquina: disparo aleatorio sin repetir casilla.
#Comprobar el final tras cada disparo: si a un jugador le quedan 0 casillas con barco, la partida termina y gana el otro.
#Mensaje final con el ganador.

import variables as v
import funciones as f
from clases import Tablero
import numpy as np

def pedir_coordenada():
    """Pide fila y columna al usuario hasta que sean válidas (0-9)."""
    while True:
        entrada = input("Introduce fila,columna (0-{v.TAMAÑO_TABLERO - 1}): ")
        partes = entrada.strip().replace(",", " ").split()

        if len(partes) != 2 or not all (p.isdecimal() for p in partes):
            print("Entrada no válida. Escribe dos números, por ejemplo: 3,5")
            continue

        fila, columna = int(partes[0]), int(partes[1])
        if not (0 <= fila < v.TAMANO_TABLERO and 0 <= columna < v.TAMANO_TABLERO):
            print(v.MENSAJES_FIJOS["fuera"])
            continue

        return fila, columna

def quedan_barcos(tablero):
    """True si al tablero todavía le queda alguna casilla de barco sin tocar."""
    return bool(np.any(tablero.tablero == v.SIMBOLOS["barco"]))

def mostrar_tableros(tablero_jugador, tablero_maquina):
    """Muestra tu tablero completo y el de la máquina solo con tus disparos."""
    print("\nTu tablero:")
    for fila in tablero_jugador.tablero:
        print(" ".join(fila))
    print("\nTablero de la máquina:")
    for fila in tablero_maquina.disparos:
        print(" ".join(fila))
    print()

def turno_jugador(tablero_jugador, tablero_maquina):
    """Turno del usuario. Devuelve True si fana la partida con este turno."""
    while True:
        fila, columna = pedir_coordenada()

        # funciones.py avisa por pantalla si es repetido; devuelve None
        if f.disparo_usuario(columna, fila) is None:
            continue

        resultado = tablero_maquina.recibir_disparo(columna, fila)
        print(resultado)
        mostrar_tableros(tablero_jugador, tablero_maquina)

        if not quedan_barcos(tablero_maquina):
            return True
        if resultado == v.MENSAJES_FIJOS["agua"]:
            return False
        # tocado o hundido: se repite turno        

def turno_maquina(tablero_jugador, tablero_maquina):
    """Turno de la máquina. Devuelve True si gana la partida con este turno."""
    print("Turno de la máquina...")
    while True:
        x, y = f.disparo_maquina()   # x = columna, y = fila
        resultado = tablero_jugador.recibir_disparo(x, y)
        print(f"La máquina: {resultado}")
        mostrar_tableros(tablero_jugador, tablero_maquina)

        if not quedan_barcos(tablero_jugador):
            return True
        if resultado == v.MENSAJES_FIJOS["agua"]:
            return False

def jugar():
    f. instrucciones()

    tablero_jugador = Tablero("jugador")
    tablero_maquina = Tablero("maquina")
    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    mostrar_tableros(tablero_jugador, tablero_maquina)

    while True:
        if turno_jugador(tablero_jugador, tablero_maquina):
            print(v.MENSAJES_FIJOS["victoria"])
            break
        if turno_maquina(tablero_jugador, tablero_maquina):
            print(v.MENSAJES_FIJOS["derrota"])
            break

if __name__ == "__main__":
    jugar()
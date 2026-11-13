NOMBRE_PROYECTO = "Hundir_la_flota"
TAMANO_TABLERO = 10
BARCOS = [4,3,2,1]
ESLORAS = [1,2,3,4]
MENSAJES_FIJOS = {
    "agua":"Agua", #Cuando el usuario lanza un misil en el agua
    "tocado":"¡Tocado!", #Cuando el usuario lanza un misil y toca parte de la flota enemiga
    "hundido": "¡Tocado y hundido!", #Cuando el usuario derrota por completo una flota enemiga
    "repetido": "Ya has disparado en esa casilla",
    "fuera": "Coordenadas fuera del tablero",
    "ocupada": "La casilla ya está ocupada",
    "victoria": "¡Has ganado!",
    "derrota": "Has perdido"}
SIMBOLOS={
    "agua":"~", #casilla sin descubrir o esta vacia
    "barco": "O", #casilla con barco
    "tocado": "X", # disparo que ha dado en un barco
    "fallo": "-" #disparo al agua
}
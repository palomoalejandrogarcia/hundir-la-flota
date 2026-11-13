NOMBRE_PROYECTO = "Hundir_la_flota"
TAMANO_TABLERO = 10
BARCOS = [4,3,2,1] #Barcos de cada eslora
ESLORAS = [1,2,3,4] #Tamaño de cada tipo de barco
MENSAJES_FIJOS = {
    "agua":"Agua", #Cuando el usuario lanza un misil en el agua
    "tocado":"¡Tocado!", #Cuando el usuario da en un barco
    "hundido": "¡Tocado y hundido!", #Cuando el usuario acaba con todas 
    "repetido": "Ya has disparado en esa casilla", #Cuando el usuario ya ha disparado en una casilla e intenta volver a disparar en esa casilla
    "fuera": "Coordenadas fuera del tablero", #Cuando el usuario dispara un misil fuera del tablero
    "ocupada": "La casilla ya está ocupada", #Cuando el usuario coloca un barco sobre otro
    "victoria": "¡Has ganado!", #Cuando el usuario gana la partida
    "derrota": "Has perdido"} #Cuando el usuario pierde la partida
SIMBOLOS = {
    "agua":"~", #casilla sin descubrir o esta vacia
    "barco": "O", #casilla con barco
    "tocado": "X", # disparo que ha dado en un barco
    "fallo": "-"} #disparo al agua
import variables 
import random
historial_maquina={}
historial_usuario={}
#La funcion disparo_maquina es que genera de manera aleatoria el disparo y se guarda en un diccionario el historial por turnos donde ha disparado
#para detectar que ha disparado en una casilla que ya ha disparado y que vuelva a disparar. Cuando termine de disparar devuelve las coordenadas de donde ha tirado 
def disparo_maquina():
    while True:
        x=random.randint(0,variables.TAMANO_TABLERO-1)
        y=random.randint(0,variables.TAMANO_TABLERO-1)
        if [x,y] in historial_maquina.values():
            continue
        else:
            print(f"Se ha disparado en las siguientes coordenadas x: {x}, y: {y}")
            historial_maquina[len(historial_maquina)+1]=[x,y]
            #print(historial_maquina)
            return x,y
# Registra el disparo del usuario en el historial.
# Si la casilla ya se había disparado, avisa y devuelve None sin guardar nada.
def disparo_usuario(x,y):
    if (x>=0 and x<=variables.TAMANO_TABLERO-1) and (y>=0 and y<=variables.TAMANO_TABLERO-1):    
            if [x,y] in historial_usuario.values():
                print(f"Usuario: {variables.MENSAJES_FIJOS['repetido']}")
                return None
            else:
                print(f"Se ha disparado en las siguientes coordenadas x: {x}, y: {y}")
                historial_usuario[len(historial_usuario)+1]=[x,y]
                #print(historial_usuario)
                return x,y
    else:
        print(f"Usuario: {variables.MENSAJES_FIJOS['fuera']}")
        return None
    
#Muestra las instrucciones del juego al usuario antes de empezar la partida
def instrucciones():
    print(f"Cada jugador tiene un tablero de {variables.TAMANO_TABLERO} x {variables.TAMANO_TABLERO}.\n"
            "Al empezar, los barcos se colocan de forma aleatoria en los dos tableros.\n"
            "Se juega por turnos y empieza el jugador.\n"
            "En cada turno se dispara a una coordenada del tablero rival.\n"
            "Para disparar, introduce las coordenadas x e y por la terminal.\n"
            "Si aciertas, vuelves a disparar. Si das en el agua, pasa el turno al rival.\n"
            "Gana quien hunda primero todos los barcos del rival y la partida termina.")    

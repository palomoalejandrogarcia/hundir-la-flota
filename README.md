# Hundir la flota

Proyecto grupal de The Bridge Data Science. Juego de terminal en Python contra una máquina, con tableros de NumPy.

## Instalación en Mac y ejecución

Requisitos: Python 3 compatible con la versión de NumPy de requirements.txt, Git y una terminal.

```bash
git clone https://github.com/palomoalejandrogarcia/hundir-la-flota.git
cd hundir-la-flota
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Si ya tienes el repositorio, actualiza tu copia desde un árbol de trabajo limpio con `git pull --ff-only origin main`.

## Cómo jugar

- Cada participante tiene un tablero de 10 × 10 con barcos colocados al azar.
- La flota tiene cuatro barcos de una casilla, tres de dos, dos de tres y uno de cuatro: 20 casillas en total.
- Los barcos tienen una casilla de separación, también en diagonal.
- Empieza el jugador. Introduce `fila,columna`, por ejemplo `3,5`. También se admite `3 5`.
- La primera coordenada es la fila vertical y la segunda es la columna horizontal. Ambas van de 0 a 9.
- Texto, coordenadas incompletas o valores fuera del tablero muestran un aviso y permiten volver a intentarlo.
- Un acierto permite volver a disparar. Hundir un barco también conserva el turno.
- Repetir una casilla conserva el turno. Si das en agua, juega la máquina.
- La máquina elige coordenadas al azar sin repetir y sigue disparando mientras acierte.
- Gana quien destruya todas las casillas de los barcos rivales. La partida termina inmediatamente tras el último acierto.

Tu tablero muestra tus barcos. El tablero de la máquina muestra únicamente los disparos realizados.

| Símbolo | Significado |
| --- | --- |
| `~` | Agua o casilla todavía sin descubrir |
| `O` | Barco propio |
| `X` | Impacto |
| `-` | Disparo al agua |

## Archivos y coordinación

| Archivo | Responsabilidad |
| --- | --- |
| `variables.py` | Constantes, mensajes y símbolos preparados por Alejandro |
| `clases.py` | Clase Tablero desarrollada por Marina |
| `funciones.py` | Disparos e instrucciones de Alejandro, entrada validada de Dario |
| `main.py` | Bucle de partida y turnos desarrollado por Luz, conectado a la entrada común |
| `requirements.txt` | Dependencias |
| `AI_LOG.md` | Registro de asistencia de IA |

La documentación se comparte entre Marina y Dario. Esta actualización aporta instalación, reglas y explicación de coordenadas.

### Orden de las coordenadas

`pedir_coordenadas()` devuelve `(fila, columna)`. El método de Marina recibe `recibir_disparo(columna, fila)`. El turno de Luz adapta el orden al llamar al método:

```python
fila, columna = f.pedir_coordenadas()
resultado = tablero_maquina.recibir_disparo(columna, fila)
```

El método devuelve el texto de `MENSAJES_FIJOS`, como `"Agua"` o `"¡Tocado!"`. El bucle compara ese texto con `MENSAJES_FIJOS["agua"]` para decidir si cambia el turno.

## Comprobaciones de esta contribución

Comprobaciones de funcionamiento:

- `0,9` devuelve `(0, 9)` con una única petición.
- `hola`, `3`, `-1,0` y `10,0` producen avisos y permiten terminar con `3,5`.
- Se mantiene la entrada por espacios que ya aceptaba main.py.
- Un impacto en `0,9` actualiza la fila 0 y la columna 9.
- Aciertos y repetidos conservan el turno, agua lo cede y el último acierto termina la partida.
- 100 flotas aleatorias contienen 20 casillas y conservan la separación.
- 100 disparos de la máquina son distintos.
- Tres partidas completas se ejecutan con entradas simuladas a través de main.py.

Las pruebas automatizadas complementan la demo manual del equipo.

## Flujo de GitHub

Trabajamos en una rama por tarea y proponemos los cambios mediante Pull Request hacia `main`. Una persona diferente revisa la PR. La contribución de validación corresponde a la issue #3 y se relaciona con la issue compartida #5.

## Guion breve para la demo

1. Mostrar los archivos y explicar la clase Tablero, las funciones y el bucle principal.
2. Ejecutar `python main.py` e introducir una entrada incorrecta.
3. Introducir una coordenada válida y explicar el resultado y el cambio o repetición de turno.
4. Mostrar que el tablero rival mantiene sus barcos ocultos.
5. Explicar el orden fila/columna, las comprobaciones realizadas y el trabajo con ramas y PR.

La explicación de los cambios y el guion para presentar están en [GUIA_PRESENTACION.md](GUIA_PRESENTACION.md).

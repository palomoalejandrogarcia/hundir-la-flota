# Guía de presentación

## Qué aporta esta entrega

La base del juego ya estaba hecha por el equipo. Alejandro preparó las constantes y las funciones de disparo, Marina la clase Tablero y Luz el flujo de la partida. La aportación de esta rama es validar la entrada del jugador, conectarla al juego y completar la documentación. También incluye un ajuste de la flota y la limpieza de los historiales.

## funciones.py: pedir_coordenadas()

1. `while True` repite la petición hasta recibir una entrada válida.
2. `input()` recibe texto, por ejemplo `3,5`.
3. `strip()` quita espacios de los extremos, `replace()` cambia las comas por espacios y `split()` separa los valores. También acepta `3 5`, como la entrada anterior.
4. Se comprueba que haya dos valores.
5. `int()` convierte los dos valores a enteros. `try/except ValueError` evita que el juego termine si se escribe texto.
6. Se comprueba que ambos estén entre cero y el tamaño del tablero menos uno.
7. `return fila, columna` entrega los números al turno del jugador.

Se usa una función para tener la validación en un solo sitio. No se usa `eval()` porque solo necesitamos convertir dos números. Se captura `ValueError` porque es el error de una conversión no válida, sin ocultar otros fallos.

## main.py: conexión con el juego

`pedir_coordenada()` conserva el nombre que ya utilizaba el main de Luz y llama a `f.pedir_coordenadas()`. Así se reutiliza la función común sin rehacer el bucle.

La entrada devuelve fila y columna, pero `recibir_disparo()` de Marina recibe columna y fila. Por eso se cambia el orden al llamar al método. Por ejemplo, `0,9` debe disparar a la fila cero, columna nueve, y se llama a `recibir_disparo(9, 0)`.

`disparo_usuario()` de Alejandro guarda las coordenadas y devuelve `None` si están repetidas. El `continue` vuelve a pedir una casilla sin perder turno.

El método del tablero devuelve los mensajes definidos en `MENSAJES_FIJOS`. Si devuelve agua, termina el turno. Si es tocado o hundido, el bucle continúa. La victoria se comprueba antes de pedir otra entrada para terminar en el último impacto.

En `jugar()` se vacían ambos historiales con `clear()`. Esto permite iniciar otra partida en el mismo proceso sin arrastrar disparos anteriores. El resto del flujo sigue siendo el de Luz.

## clases.py: ajuste de la flota

Antes se recorría `ESLORAS`, que contiene `[1, 2, 3, 4]`. Eso colocaba un barco de cada tamaño: diez casillas en total.

Ahora `zip(BARCOS, ESLORAS)` junta cada cantidad con su tamaño. Se prepara una lista con cuatro barcos de uno, tres de dos, dos de tres y uno de cuatro. La suma es `4*1 + 3*2 + 2*3 + 1*4 = 20`.

`sorted(..., reverse=True)` coloca primero los grandes, que necesitan más espacio. Se conserva la lógica de Marina para elegir posiciones, comprobar límites y separar barcos. Este cambio reduce el problema de quedarse sin espacio para los grandes; el algoritmo mantiene intentos aleatorios sin un límite, por lo que no es una garantía matemática de terminación para cualquier configuración.

## Por qué mantener la estructura del equipo

| Decisión | Motivo |
| --- | --- |
| Conservar los diccionarios de historial | Ya los utilizan las funciones de Alejandro y permiten detectar disparos repetidos |
| Conservar la clase Tablero | Ya reúne los tableros, barcos y resultados de disparo |
| Mantener los mensajes de variables.py | Evita escribir mensajes distintos en cada archivo |
| Usar el tamaño definido en variables.py | Evita repetir el número 10 en la validación |
| Mantener el juego por terminal | Permite centrarse en Python y NumPy con una presentación sencilla |
| Mantener pedir_coordenada() | Conserva la llamada existente del main y delega la validación |

## Comprobaciones y demo

Para instalar y ejecutar, seguir el README. En la presentación:

1. Mostrar `variables.py`, `clases.py`, `funciones.py` y `main.py`, indicando el trabajo de cada persona.
2. Ejecutar `python main.py`.
3. Escribir `hola`, después `3`, después `-1,0` y `10,0`. Debe avisar y volver a pedir coordenadas.
4. Escribir `0,9`. Mostrar que la primera coordenada es la fila y la segunda la columna.
5. Repetir una coordenada cuando vuelva a tocar al jugador. Debe avisar y dejar elegir otra.
6. Explicar que un impacto conserva el turno y agua lo cede. Los barcos son aleatorios, por lo que no hay una coordenada fija que garantice un impacto en la demo.
7. Mostrar que el tablero rival solo enseña disparos, no barcos ocultos.
8. Enseñar la PR #16 y el reparto de archivos. El registro de IA está en AI_LOG.md.

Las comprobaciones automáticas cubren entradas incorrectas, orden de coordenadas, repetidos, agua, victoria y generación de flotas. No sustituyen que el equipo ejecute la demo antes de presentar.

## Texto breve para quien lo presente

“La aportación de Dario se centra en la entrada del jugador y su integración. La función pide dos coordenadas, comprueba que sean enteros y que estén dentro del tablero. Si hay un error, vuelve a pedirlas. Se conserva el código de disparos, tableros y turnos del equipo. También se ajustó la colocación para respetar las cantidades de barcos del enunciado y se documentó cómo instalar, jugar y comprobar el programa. El apoyo de IA utilizado queda recogido en el registro del proyecto.”

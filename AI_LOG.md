# Registro de uso de IA
## Herramienta
ChatGPT / Codex para la contribución de Dario del 23/11/2026.
## Registro

| Fecha | Tarea | Qué se pidió | Qué se hizo con la respuesta |
|---|---|---|---|
| 16/11/2026 | variables.py | Revisar constantes, mensajes y símbolos | Se aplicaron las sugerencias de nombres y comentarios |
| 23/11/2026 | Contribución de Dario, issue #3 y README | Revisar el código fusionado de Alejandro, Marina y Luz, completar la entrada y documentar el proyecto | Codex implementó pedir_coordenadas(), conectó el validador al main existente y documentó instalación, reglas, coordenadas y autoría. Conservó recibir_disparo(columna, fila) y sus mensajes completos. Corrigió la cantidad de barcos para usar BARCOS y ESLORAS y colocar 20 casillas, primero las esloras grandes. Añadió limpieza de historiales al arrancar otra partida. |
| 23/11/2026 | Verificación automatizada de Codex | Comprobar lo implementado realmente | Ejecutadas entradas 0,9, hola, 3, -1,0, 10,0 y 3,5, compatibilidad con espacios, orden de coordenadas, acierto/repetido/agua y victoria inmediata, 100 flotas de 20 casillas con separación, 100 disparos de máquina distintos y tres partidas completas con entrada simulada. Compilación y pruebas repetidas en un entorno limpio con numpy==2.5.4 instalado desde requirements.txt. |

## Reflexión
- Qué me ayudó.
- Qué tuve que corregir o decidir yo.

### Contribución asistida de Dario del 23/11/2026

- La revisión del código existente permitió reutilizar el bucle de Luz y el contrato de coordenadas de Marina.
- Se mantuvo pedir_coordenada() en main.py como llamada a la función común de funciones.py para conservar su uso anterior.
- La colocación inicial solo recorría ESLORAS y creaba 10 casillas. Se aplicaron también las cantidades de BARCOS para crear las 20 requeridas.
- Al probar la flota completa, colocar primero las esloras pequeñas podía bloquear la búsqueda de espacio. Se ordenaron las esloras de mayor a menor, conservando la separación de Marina.
- Las verificaciones aquí descritas las ejecutó Codex. Dario debe revisar y comprender la contribución y realizar su demo manual.

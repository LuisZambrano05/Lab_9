"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] > objetivo:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)
    else:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)



# ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#   Situación A: Cuando encontramos el número (codigos[medio] == objetivo)
#   Situación B: Cuando la 'izquierda' se cruza y se vuelve mayor que la 
#   'derecha' (izquierda > derecha), significa que ya no hay donde buscar.
# ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
#   Porque ya revisamos la posición del 'medio' y sabemos  no está ahí.
#  Si la volvemos a incluir, nos
#   podríamos quedar atrapados en un ciclo infinito revisando lo mismo.
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |     0     |    6    |   3   | Como 415 > 300, ir a la izquierda.
#       2    |     0     |    2    |   1   | Como 205 < 300, ir a la derecha.
#       3    |     2     |    2    |   2   | Como 310 > 300, ir a la izquierda.
#       4    |     2     |    1    |   —   | izquierda > derecha, devolver -1.
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
#   En 'contar_desde_limite' el problema se reduce de UNO en UNO (lento).
#   En 'buscar_codigo' el problema se reduce a la MITAD de golpe en cada 
#   llamada (rapidísimo).
#


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
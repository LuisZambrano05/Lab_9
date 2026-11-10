"""
Ejercicio 5. Extraer valores de una estructura anidada

Un sistema recibe mediciones agrupadas en listas que pueden contener otras
listas, con distintos niveles de profundidad.

    def extraer_valores(datos):
        pass

La función devuelve una nueva lista plana con todos los números, en el orden en
que aparecen de izquierda a derecha. Las entradas contienen únicamente números
y listas, y no tienen referencias cíclicas.

Ejemplos

    extraer_valores([10, [20, 30], 40])     # [10, 20, 30, 40]
    extraer_valores([1, [2, [], [3]], 4])   # [1, 2, 3, 4]
    extraer_valores([[], [[], []]])         # []
    extraer_valores([])                     # []

Requisitos

- Utiliza un ciclo para recorrer los elementos del nivel actual.
- Si encuentras un número, incorpóralo al resultado.
- Si encuentras una lista, procésala mediante una llamada recursiva.
- Puedes utilizar append() y extend().
- No utilices cortes.
- No modifiques la estructura original.
- No dejes sublistas dentro del resultado.
"""


def extraer_valores(datos):
    resultado = []
    for elemento in datos:
        if isinstance(elemento, list):
            resultado.extend(extraer_valores(elemento))
        else:
            resultado.append(elemento)
    return resultado
                  # []

# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué devuelve la función cuando recibe una lista vacía?
#devuelve una lista vacia []
#
# 2. ¿Qué diferencia hay entre incorporar un número e incorporar el
#    resultado de una llamada recursiva?
#el numero se agrega con append y el resultado de la llamada recursiba es una sublista por lo que se usa extend para desarmar y fusionar los elementos de la lista principal
#
# 3. Dibuja únicamente las llamadas a extraer_valores() para
#    [1, [2, [], [1]], 4]. ¿Cuántas llamadas se realizan, incluyendo las
#    de listas vacías?
#- Llamada 1: extraer_valores([1, [2, [], [1]], 4])          (Lista principal)
#   - Llamada 2: extraer_valores([2, [], [1]])                (Sublista interna)
#     - Llamada 3: extraer_valores([])                        (Sublista vacía)
#     - Llamada 4: extraer_valores([1])                         (Sublista con el 1)
#se hacen 4 llamadas a la funcion
# 4. ¿Por qué cada llamada necesita su propia lista de resultados?
#
#porque cada sublista agarra los numeros y arma su propia coleccion de numerosde forma independiente 


if __name__ == "__main__":
    print(extraer_valores([10, [20, 30], 40]))     # [10, 20, 30, 40]
    print(extraer_valores([1, [2, [], [3]], 4]))   # [1, 2, 3, 4]
    print(extraer_valores([[], [[], []]]))         # []
    print(extraer_valores([]))                     # []

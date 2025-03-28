# Ejercicio 1

Aquí está la lección de 6.00.1x sobre generadores. Además, también puedes echar un vistazo al Capítulo 8.3 del libro de texto.

Para el siguiente problema, considera la siguiente forma de escribir un generador de conjunto de potencia. El número de combinaciones posibles para poner n elementos en una bolsa es 2^N. Aquí, `items` es una lista de Python. Si es necesario, consulta también la documentación sobre operadores a nivel de bits (`<<`, `>>`, `&`, `|`, `~`, `^`).

```python
# generar todas las combinaciones de N elementos
def powerSet(items):
    N = len(items)
    # enumerar las 2**N posibles combinaciones
    for i in range(2**N):
        combo = []
        for j in range(N):
            # probar el bit j del entero i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
```

Como se indicó anteriormente, supongamos que tenemos un generador que devuelve cada combinación de objetos en una bolsa. Podemos representar esto como una lista de 1s y 0s que indican si cada elemento está en la bolsa o no.

Escribe un generador que devuelva cada disposición de elementos de modo que cada uno esté en una o ninguna de dos bolsas diferentes. Cada combinación debe proporcionarse como una tupla de dos listas, la primera siendo los elementos en `bag1` y la segunda los elementos en `bag2`.

```python
def yieldAllCombos(items):
    """
      Genera todas las combinaciones de N elementos en dos bolsas, 
      donde cada elemento está en una o cero bolsas.

      Devuelve una tupla, (bag1, bag2), donde cada bolsa se representa 
      como una lista de qué elemento(s) están en cada bolsa.
    """
```

Ten en cuenta que este generador debe ser bastante similar al generador `powerSet` anterior.

Mencionamos que el número de combinaciones posibles para N elementos en una bolsa es 2^N. ¿Cuántas combinaciones posibles existen cuando hay dos bolsas? Piensa en esto durante unos minutos y luego haz clic en la siguiente pista para confirmar si tu suposición es correcta. Recuerda que un elemento dado solo puede estar en `bag1`, `bag2` o en ninguna bolsa: ¡no es posible que un elemento esté presente en ambas bolsas!
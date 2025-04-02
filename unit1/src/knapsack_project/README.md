# Resumen: Modelos de Optimización y el Problema de la Mochila

Este resumen cubre los conceptos clave presentados sobre modelos de optimización, utilizando el problema de la mochila (Knapsack Problem) como ejemplo principal.

## ¿Qué son los Modelos de Optimización?

*   **Concepto:** Una forma estructurada de resolver problemas computacionales buscando el "mejor" resultado (máximo, mínimo, más rápido, más barato, etc.).
*   **Componentes Clave:**
    1.  **Función Objetivo:** La cantidad que se desea maximizar o minimizar (ej: minimizar tiempo de viaje, maximizar placer al comer).
    2.  **Restricciones (Constraints):** Condiciones que deben cumplirse (ej: no gastar más de $100, no exceder 1500 calorías, llegar antes de las 5 PM). Pueden ser opcionales (conjunto vacío).
*   **Importancia:**
    *   Muchos problemas del mundo real (viajes, logística, finanzas, dietas) pueden formularse como problemas de optimización.
    *   Es más fácil mapear un problema a uno ya conocido y resuelto que inventar una solución desde cero.
    *   Los problemas de optimización suelen ser computacionalmente "difíciles" (pueden tardar mucho tiempo en resolverse de forma exacta).

## El Problema de la Mochila (Knapsack Problem)

Es un problema clásico de optimización usado como ejemplo recurrente.

*   **Descripción:** Tienes una mochila con capacidad limitada (peso, volumen, calorías, etc.) y un conjunto de objetos, cada uno con un valor y un "peso". Debes decidir qué objetos meter en la mochila para maximizar el valor total sin exceder la capacidad.
*   **Variantes:**
    *   **0/1 Knapsack Problem:** Debes decidir si tomar un objeto completo (1) o no tomarlo (0). No puedes tomar fracciones. (Ej: robar un cuadro entero o nada). Es computacionalmente más difícil.
    *   **Continuo o Fraccional Knapsack Problem:** Puedes tomar partes de un objeto. (Ej: llevar polvo de oro, comer parte de un plato). Es más fácil de resolver (similar a llenar con "polvo de oro" hasta el límite).
*   **Formalización (para 0/1):**
    *   Cada ítem `i` se representa por `(valor_i, peso_i)`.
    *   Capacidad máxima de la mochila: `W`.
    *   Conjunto de `n` ítems disponibles.
    *   Vector `v` de longitud `n`, donde `v[i] = 1` si se toma el ítem `i`, y `v[i] = 0` si no.
    *   **Objetivo:** Maximizar `Σ (v[i] * valor_i)` para todos los ítems `i`.
    *   **Restricción:** `Σ (v[i] * peso_i) ≤ W` para todos los ítems `i`.

## Estrategias de Solución

Se exploran diferentes enfoques para resolver el problema de la mochila 0/1.

### 1. Fuerza Bruta (Enumeración Exhaustiva / Árbol de Búsqueda)

*   **Concepto:** Generar todas las combinaciones posibles de ítems (el conjunto potencia o *power set*).
*   **Pasos:**
    1.  Enumerar todos los subconjuntos de ítems.
    2.  Eliminar los subconjuntos cuyo peso total excede `W`.
    3.  De los restantes, elegir uno (o varios) con el máximo valor total.
*   **Implementación (Árbol de Búsqueda):**
    *   Se construye un árbol de decisión donde cada nivel representa un ítem.
    *   Cada nodo tiene dos ramas: "tomar" el ítem (izquierda) y "no tomar" el ítem (derecha).
    *   Se explora el árbol (ej: búsqueda en profundidad primero por la izquierda - DFS).
    *   Se pueden podar ramas que violen la restricción de peso.
*   **Complejidad:** Exponencial (O(2^n)), donde `n` es el número de ítems. Esto lo hace impracticable para conjuntos grandes de ítems (ej: n=100 es inviable).
*   **Viabilidad:** Solo útil para problemas muy pequeños. Aunque garantiza la solución óptima.

### 2. Algoritmos Voraces (Greedy Algorithms)

*   **Concepto:** En lugar de buscar la solución óptima global (que es costosa), se toman decisiones *localmente óptimas* en cada paso con la esperanza de llegar a una solución *suficientemente buena*. Es una **aproximación**.
*   **Algoritmo Básico:** Mientras la mochila no esté llena, añadir el "mejor" ítem disponible.
*   **Definición de "Mejor":** Esto es crucial y variable. Puede ser:
    *   El de mayor valor.
    *   El de menor "costo" (peso/calorías).
    *   El de mayor "densidad" (valor / costo).
*   **Implementación:**
    *   Requiere una forma flexible de definir "mejor" (ej: usando una `key_function`).
    *   Se ordenan los ítems según el criterio elegido (de mejor a peor).
    *   Se itera sobre la lista ordenada, añadiendo ítems si caben.
    *   Se usa `lambda` para crear funciones clave simples al vuelo (ej: para ordenar por costo inverso).
*   **Complejidad:** Eficiente. Dominada por la ordenación (O(N log N)).
*   **Limitaciones:**
    *   **No garantiza la solución óptima.** Una secuencia de decisiones localmente óptimas no siempre lleva al óptimo global (analogía de escalar la colina: puedes quedar atrapado en un óptimo local).
    *   Diferentes criterios de "mejor" pueden dar resultados distintos, y ninguno es universalmente superior.

### 3. Programación Dinámica

*   **Motivación:** Buscar una solución *óptima* de forma más eficiente que la fuerza bruta, especialmente cuando esta última es demasiado lenta.
*   **Idea Clave: Memoización**
    *   Observar que en la solución recursiva (como el árbol de búsqueda), se resuelven los mismos subproblemas múltiples veces.
    *   Guardar (memorizar) los resultados de los subproblemas ya calculados en una tabla o diccionario (`memo`).
    *   Antes de calcular un subproblema, verificar si ya está en la `memo`. Si es así, devolver el resultado guardado; si no, calcularlo, guardarlo y devolverlo.
    *   Se "intercambia espacio por tiempo".
*   **Ejemplo Ilustrativo: Fibonacci**
    *   La implementación recursiva ingenua es exponencial porque recalcula `fib(k)` muchas veces.
    *   Con memoización, `fib(k)` solo se calcula una vez. La complejidad se reduce drásticamente.
*   **Condiciones de Aplicación:** La programación dinámica funciona bien si el problema tiene:
    1.  **Subestructura Óptima:** Una solución óptima global se puede construir a partir de soluciones óptimas de subproblemas locales. (El problema de la mochila lo tiene).
    2.  **Subproblemas Superpuestos (Overlapping Subproblems):** La solución recursiva resuelve los *mismos* subproblemas repetidamente.
*   **Aplicación a la Mochila:**
    *   ¿Hay subproblemas superpuestos? ¡Sí! El estado de un subproblema se define por los *ítems que quedan por considerar* y la *capacidad restante* en la mochila. Es posible llegar al mismo estado (mismos ítems restantes, misma capacidad restante) a través de diferentes secuencias de decisiones (diferentes ítems ya elegidos).
    *   **Implementación:** Modificar la función recursiva de fuerza bruta (árbol de búsqueda) para incluir un parámetro `memo` (diccionario).
        *   La clave de la `memo` suele ser una tupla que representa el estado: `(ítems_restantes, capacidad_restante)`.
        *   `ítems_restantes` puede representarse eficientemente (ej: por la longitud de la lista restante si siempre se procesa desde el inicio).
*   **Rendimiento:** Mejora drásticamente el rendimiento en la práctica comparado con la fuerza bruta, permitiendo resolver problemas mucho más grandes.
*   **Complejidad (Sutileza):** Aunque mucho mejor, la complejidad no es estrictamente polinomial respecto a `n`. Es *pseudo-polinomial*. Su tiempo de ejecución depende también del valor numérico de la capacidad `W`. En el peor de los casos (poca superposición de subproblemas), podría seguir siendo exponencial, pero en la práctica suele ser muy eficiente.
*   **Detalle Técnico:** La recursión profunda puede exceder el límite de recursión de Python. Se puede ajustar con `sys.setrecursionlimit()`.

## Conclusiones Clave

1.  La **optimización** es un marco poderoso para resolver problemas prácticos.
2.  El **problema de la mochila** es un ejemplo canónico que ilustra diferentes enfoques.
3.  Los **algoritmos voraces** son rápidos y fáciles, buenos para aproximaciones, pero no garantizan optimalidad.
4.  La **fuerza bruta** garantiza optimalidad pero es computacionalmente inviable para tamaños grandes.
5.  La **programación dinámica** (con memoización) ofrece una vía para encontrar soluciones óptimas de forma mucho más eficiente que la fuerza bruta para problemas con subestructura óptima y subproblemas superpuestos, como a menudo ocurre en la práctica con el problema de la mochila.
# Ejercicio de Optimización: Algoritmo de Selección de Botín

## Contexto del Problema

Un ladrón encuentra los siguientes objetos durante un robo:

| Objeto       | Peso | Valor |
|--------------|------|-------|
| Tierra       | 4    | 0     |
| Computadora  | 10   | 30    |
| Tenedor      | 5    | 1     |
| Problema     | 0    | -10   |

**Restricciones:**
- Capacidad máxima de peso: 14
- Objetivo: Maximizar la relación valor-peso de los objetos transportados

## Algoritmo de Selección

El algoritmo funciona en dos pasos principales:

1. Evaluar la métrica de cada elemento
2. Agregar elementos al botín desde el valor de métrica más alto hasta el más bajo, respetando la capacidad de peso

## Métricas de Evaluación

### Métrica 1

```python
def metric1(item):
    return item.getValue() / item.getWeight() 
```

#### Preguntas
- **Heurística empleada:**
  - [ ] Elegir el objeto más ligero primero
  - [ ] Elegir el objeto más valioso primero
  - [x] Elegir el elemento con la mejor relación valor-peso primero

- **Resultado de ejecutar el algoritmo:**
  - [ ] El algoritmo se ejecuta y devuelve la solución óptima
  - [ ] El algoritmo se ejecuta y devuelve una solución no óptima
  - [x] El algoritmo no se ejecuta

### Métrica 2

```python
def metric2(item):
    return  -item.getWeight()
```

#### Preguntas
- **Heurística empleada:**
  - [x] Elegir el objeto más ligero primero
  - [ ] Elegir el objeto más valioso primero
  - [ ] Elegir el elemento con la mejor relación valor-peso primero

- **Resultado de ejecutar el algoritmo:**
  - [ ] El algoritmo se ejecuta y devuelve la solución óptima
  - [x] El algoritmo se ejecuta y devuelve una solución no óptima
  - [ ] El algoritmo no se ejecuta

### Métrica 3

```python
def metric3(item):
    return item.getValue()
```

#### Preguntas
- **Heurística empleada:**
  - [ ] Elegir el objeto más ligero primero
  - [x] Elegir el objeto más valioso primero
  - [ ] Elegir el elemento con la mejor relación valor-peso primero

- **Resultado de ejecutar el algoritmo:**
  - [ ] El algoritmo se ejecuta y devuelve la solución óptima
  - [x] El algoritmo se ejecuta y devuelve una solución no óptima
  - [ ] El algoritmo no se ejecuta

## Consideraciones Finales

Este ejercicio explora diferentes estrategias de optimización y selección bajo restricciones de peso, ilustrando cómo distintas métricas pueden influir en la toma de decisiones.
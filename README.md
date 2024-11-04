# Spark RDD - Transformaciones y Acciones

Este repositorio proporciona ejemplos básicos de transformaciones y acciones en Apache Spark usando RDDs (Resilient Distributed Datasets). Cada transformación y acción tiene su propio archivo en las carpetas `transformaciones/` y `accciones/`.

## Contenidos
- **Transformaciones**: Operaciones que crean un nuevo RDD a partir de uno existente.
- **Acciones**: Operaciones que ejecutan el cálculo en el RDD y devuelven un valor al driver.

## Requisitos
- Apache Spark
- Python o Scala

## Ejecución
Para ejecutar cada ejemplo, asegúrate de tener Apache Spark instalado y ejecuta cada archivo `.py` desde la línea de comandos.

## Transformaciones
- [map.py](transformaciones/map.py): Ejemplo de transformación `map`, que aplica una función a cada elemento del RDD.
- [filter.py](transformaciones/filter.py): Ejemplo de transformación `filter`, que filtra elementos según una condición.
- [flatMap.py](transformaciones/flatMap.py): Ejemplo de transformación `flatMap`, que divide cada elemento en múltiples elementos.
- [distinct.py](transformaciones/Distinc.py): Ejemplo de la acción `distinct`, que elimina duplicados y devuelve un RDD con elementos únicos.
- [intersection.py](transformaciones/intersection.py): Ejemplo de la transformación `intersection`, que devuelve un RDD con los elementos comunes entre dos RDDs. Esta transformación es útil para identificar datos compartidos en conjuntos grandes.

  
## Acciones

- [collect.py](Acciones/collect.py): Muestra la acción `collect`, que recupera todos los elementos del RDD al controlador.
- [count.py](Acciones/count.py): Ejemplo de `count`, que cuenta el total de elementos del RDD.
- [countByKey.py](Acciones/countByKey.py): Utiliza `countByKey` para contar elementos por clave en un RDD de pares.
- [first.py](Acciones/first.py): Demuestra `first`, que devuelve el primer elemento del RDD.
- [foreach.py](Acciones/foreach.py): Aplica `foreach` para ejecutar una función en cada elemento.
- [max || min.py](Acciones/max_min.py): Encuentra el máximo y mínimo valor en el RDD.
- [reduce.py](Acciones/reduce.py): Usa `reduce` para combinar elementos del RDD iterativamente.
- [saveAsTextFile.py](Acciones/saveAsTextFile.py): Guarda el RDD en un archivo de texto.
- [take.py](Acciones/take.py): Retorna una cantidad específica de elementos del RDD.



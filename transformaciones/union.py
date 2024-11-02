from pyspark import SparkContext

sc = SparkContext("local", "Union Example")

# Datos de ejemplo: dos listas de tuplas
datos1 = [("a", 1), ("b", 2)]
datos2 = [("c", 3), ("d", 4)]

# Crear RDDs a partir de los datos
rdd1 = sc.parallelize(datos1)
rdd2 = sc.parallelize(datos2)

# Aplicamos la transformación union para combinar los RDDs
rdd_union = rdd1.union(rdd2)

# Recogemos y mostramos el resultado
print("Resultado de union:", rdd_union.collect())

sc.stop()

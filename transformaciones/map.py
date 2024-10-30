from pyspark import SparkContext

sc = SparkContext("local", "Map Example")

datos = [("a", 1), ("b", 2), ("a", 3)]
rdd = sc.parallelize(datos)

# Aplicamos la transformación map: Multiplica el valor de cada elemento por 2
rdd_map = rdd.map(lambda x: (x[0], x[1] * 2))
print("Resultado de map:", rdd_map.collect())

sc.stop()

from pyspark import SparkContext

sc = SparkContext("local", "Filter Example")

datos = [("a", 1), ("b", 2), ("a", 3), ("c", 4)]
rdd = sc.parallelize(datos)

# Aplicamos la transformación filter: Filtra los elementos donde el valor es mayor que 2
rdd_filter = rdd.filter(lambda x: x[1] > 2)
print("Resultado de filter:", rdd_filter.collect())

sc.stop()

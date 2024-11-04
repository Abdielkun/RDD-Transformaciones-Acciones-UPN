from pyspark import SparkContext

sc = SparkContext("local", "SortByKey Example")

datos = ["b", "a", "e", "c", "d", "f"]

# Creamos un RDD
rdd = sc.parallelize(datos)

# Aplicamos sortByKey para qu enos muestre ordenadod alfabeticamente
rdd_ordenado = rdd.sortByKey()

# mostramos el resultado
resultado = rdd_ordenado.collect()
print("Ordenado:", resultado)

sc.stop()

from pyspark import SparkContext

sc = SparkContext("local", "ReduceByKey Example")

# Datos
datos = [("Gato", 1), ("Pez", 1), ("Gato", 1), ("Perro", 1), ("Pez", 1), ("Perro", 1), ("Perro", 1)]

# Creamos RDDs
rdd = sc.parallelize(datos)

# Usamos reduceByKey para contabilisar
rdd_reducido = rdd.reduceByKey(lambda a, b: a + b)

# mostramos el resultado
resultado = rdd_reducido.collect()
print(":", resultado)

sc.stop()

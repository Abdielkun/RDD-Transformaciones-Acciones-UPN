from pyspark import SparkContext

sc = SparkContext("local", "Join Example")

# Datos 
datos1 = [("a", 1), ("b", 2), ("c", 3)]
datos2 = [("b", 4), ("c", 5), ("d", 6)]

# Creamos RDDs 
rdd1 = sc.parallelize(datos1)
rdd2 = sc.parallelize(datos2)

# Aplicamos join para combinar los RDDs
rdd_joined = rdd1.join(rdd2)

# mostramos el resultado
resultado = rdd_joined.collect()
print("Resultado:", resultado)

sc.stop()

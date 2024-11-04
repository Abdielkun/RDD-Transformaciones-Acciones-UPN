from pyspark import SparkContext

sc = SparkContext("local", "Union Sentences Example")

# Datos
oracion1 = ["Gato"]
oracion2 = ["Durmiendo"]

# Creamos RDDs
rdd1 = sc.parallelize(oracion1)
rdd2 = sc.parallelize(oracion2)

# combinamos los RDDs
rdd_union = rdd1.union(rdd2)

# UUnimos las palabras en una sola oración
texto_unido = " ".join(rdd_union.collect())
print("Resultado de union:", texto_unido)

sc.stop()

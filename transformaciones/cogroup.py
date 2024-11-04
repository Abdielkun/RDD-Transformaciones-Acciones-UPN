from pyspark import SparkContext

sc = SparkContext("local", "cogroup example")

# Definir dos RDDs con pares clave-valor
rdd1 = sc.parallelize([("a", 1), ("b", 2), ("a", 3)])
rdd2 = sc.parallelize([("a", "x"), ("b", "y"), ("b", "z")])

# Aplicar cogroup
cogrouped_rdd = rdd1.cogroup(rdd2)

# Mostrar el resultado
print(cogrouped_rdd.mapValues(lambda x: (list(x[0]), list(x[1]))).collect())


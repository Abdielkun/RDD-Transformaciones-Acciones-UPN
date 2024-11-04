from pyspark import SparkContext

sc = SparkContext("local", "coalesce example")

# Crear un RDD con 4 particiones
rdd = sc.parallelize(range(1, 11), 4)

print(f"Número inicial de particiones: {rdd.getNumPartitions()}")

# Reducir el número de particiones a 2
coalesced_rdd = rdd.coalesce(2)

print(f"Número de particiones después de coalesce: {coalesced_rdd.getNumPartitions()}")

# Mostrar los datos por partición
print(coalesced_rdd.glom().collect())

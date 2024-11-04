# Obtener los primeros 3 elementos de un RDD
rdd = sc.parallelize([10, 20, 30, 40, 50])
taken_elements = rdd.take(3)
print(taken_elements)  # Resultado: [10, 20, 30]

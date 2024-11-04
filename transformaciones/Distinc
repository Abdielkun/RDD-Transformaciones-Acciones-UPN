
# Crear un RDD con elementos duplicados
rdd = sc.parallelize([1, 2, 2, 3, 4, 4, 5, 6, 6])

# Aplicar el método `distinct` para eliminar duplicados
distinct_rdd = rdd.distinct()

# Recoger y mostrar los elementos únicos
result = distinct_rdd.collect()
print(result)  # Resultado: [1, 2, 3, 4, 5, 6]

# Máximo y mínimo de una lista de números
rdd = sc.parallelize([5, 1, 9, 3, 7])
max_value = rdd.max()
min_value = rdd.min()
print(max_value)  # Resultado: 9
print(min_value)  # Resultado: 1

# Contar el número de elementos por clave
rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1), ("b", 1), ("c", 1)])
count_by_key = rdd.countByKey()
print(count_by_key)  # Resultado: {'a': 2, 'b': 2, 'c': 1}

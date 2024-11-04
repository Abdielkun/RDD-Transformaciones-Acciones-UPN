from pyspark import SparkContext

sc = SparkContext("local", "GroupByKey Example")

# Datos
datos = [("Gato", 1), ("Pez", 1), ("Gato", 2), ("Perro", 1), ("Pez", 2), ("Perro", 3), ("Perro", 1)]

# Creamos un RDD 
rdd = sc.parallelize(datos)

# Aplicamos groupByKey para agrupar los valores de las categoría
rdd_grupo = rdd.groupByKey()

# mostramos el resultado
resultado = rdd_grupo.mapValues(list).collect()
print("Valores:", resultado)

sc.stop()

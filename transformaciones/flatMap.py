from pyspark import SparkContext

sc = SparkContext("local", "FlatMap Example")

# Datos de ejemplo: una lista de frases
datos = ["Hola mundo", "Aprendiendo Spark", "flatMap es útil"]

# Crear un RDD a partir de los datos
rdd = sc.parallelize(datos)

# Aplicamos la transformación flatMap: Divide cada frase en palabras
rdd_flatMap = rdd.flatMap(lambda x: x.split(" "))
print("Resultado de flatMap:", rdd_flatMap.collect())

sc.stop()

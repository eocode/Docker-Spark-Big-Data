from pyspark import SparkContext
import time

sc = SparkContext(master="local", appName="transformacionesYAcciones")

rdd1 = sc.parallelize([1, 2, 3])

path = "./../files/"

equiposOlimpicosRDD = sc.textFile(path + "paises.csv").map(lambda line: line.split(","))

equiposOlimpicosRDD.take(5)

time.sleep(300)

sc.stop()

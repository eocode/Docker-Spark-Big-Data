from pyspark import SparkContext
from pyspark.sql import SparkSession
import time
spark = SparkSession.builder.master("local").appName("miPrimerSession").getOrCreate()
spark.stop()
sc = SparkContext(master="local", appName="miPrimerContexto")
spark2 = SparkSession(sc)

time.sleep(30)

spark2
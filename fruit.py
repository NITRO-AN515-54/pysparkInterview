from pyspark.sql import SparkSession
from pyspark.sql.functions import when, sum

spark = SparkSession.builder \
    .appName("Student MaxMin") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("data/personfruit.csv", header=True, inferSchema=True)

df = df.withColumn(
    "Type",
    when((df.Fruit == "Orange") | (df.Fruit == "Apple"), 1).otherwise(0)
)

agg_df = df.groupBy("Person").agg(sum("Type").alias("TypeOfFruit"))

result = agg_df.filter(agg_df.TypeOfFruit == 2).select("Person")

result.show()

spark.stop()


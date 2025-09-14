import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Zulu\zulu-11"
os.environ["PATH"] = os.environ["JAVA_HOME"] + r"\bin;" + os.environ["PATH"]

from pyspark.sql import SparkSession
from pyspark.sql.functions import greatest, least

spark = SparkSession.builder \
    .appName("Student MaxMin") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("data/students.csv", header=True, inferSchema=True)

df = df.withColumn("Max_Score", greatest("s1", "s2", "s3", "s4")) \
       .withColumn("Min_Score", least("s1", "s2", "s3", "s4"))

df.show()

spark.stop()


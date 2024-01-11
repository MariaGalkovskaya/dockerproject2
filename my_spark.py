from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("HousePricesAnalysis") \
    .config("spark.jars", "/app/jars/postgresql-42.7.1.jar") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/house_db") \
    .option("dbtable", "public.house_prices") \
    .option("user", "Maria") \
    .option("password", "12345678") \
    .load()

result_df = df.groupBy("location", "bedrooms") \
    .agg(avg("price").alias("avg_price")) \
    .orderBy("location", "bedrooms")

result_df.show()

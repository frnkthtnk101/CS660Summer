'''
lab 6 pyspark
franco, eric, park, tod
example program that gets the taxi information an basically
gives back the stats for the fair and the tip
also see if there is an correlation (there is none)
'''

from pyspark import SparkContext
from pyspark.sql import SparkSession
#only needed for the schema.
#from pyspark.sql.types import DateType, StringType, IntegerType, StructField, StructType, DoubleType, ArrayType, MapType
sc = SparkContext("local", "taxis")
spark = SparkSession.builder.getOrCreate()
home = "/Users/francopettigrosso/ws/CS660Summer/samples/"
yellow_taxis = home+"yellow_tripdata.csv"

'''
this just didnt work
the_schema = StructType([
    StructField("VendorID", StringType()),
    StructField("tpep_pickup_datetime", StringType()),
    StructField("passenger_count", StringType()),
    StructField("trip_distance", StringType()),
    StructField("RatecodeID", StringType()),
    StructField("store_and_fwd_flag", StringType()),
    StructField("PULocationID", StringType()),
    StructField("DOLocationID", StringType()),
    StructField("payment_type", StringType()),
    StructField("fare_amount", StringType()),
    StructField("extra", StringType()),
    StructField("mta_tax", StringType()),
    StructField("tip_amount",StringType()),
    StructField("tolls_amount", StringType()),
    StructField("improvement_surcharge", StringType()),
    StructField("total_amount", StringType()),
    StructField("congestion_surcharge", StringType())
])
'''

taxis = spark.read.csv(yellow_taxis, header = True )


taxis.printSchema()

taxis.describe(['fare_amount','tip_amount']).show()

#need to convert the string columns into floats
taxis_special = taxis \
.select('fare_amount','tip_amount') \
.withColumn("fare_double", taxis['fare_amount'].cast('float')) \
.withColumn("tip_double", taxis['tip_amount'].cast('float'))


print taxis_special.columns

taxis_correlation_fare_tip = taxis_special.stat.corr('fare_double','tip_double')

print "theres is a  " + str(taxis_correlation_fare_tip) + " between the tip and the price of the fair."

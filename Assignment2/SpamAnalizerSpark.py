from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, col, regexp_replace
from pyspark.sql.types import StringType, StructField, StructType
from os import path
sc = SparkContext("local", "spam_to_ham")
spark = SparkSession.builder.getOrCreate()
home = "/Users/francopettigrosso/ws/CS660Summer/samples/"
trained_data = home+"trained_data.csv"
training_data = home+"training_data.csv"
input_text = home+"sentences.txt"
money_regex = r"\$|€|£"

'''
mama mia mama mia
first thing we need to do is create the training data
-check if we already get trained data
-clean the data
then we need to pull it throught the algorthim
-gather the training data
-gather the input sentences
-run the analysis
'''

the_trained_file_exist = path.isfile(trained_data)
if the_trained_file_exist:
    trained_data = spark.read.csv(trained_data, header = False )
else:
    the_schema = StructType([
    StructField("classified", StringType()),
    StructField("content", StringType())
    ])
    raw_data = spark.read.csv(training_data, header = False, schema = the_schema)
    raw_data.printSchema()
    raw_data.show(5)
    #clean up data...
    raw_data = raw_data \
    .withColumn('content', lower(col('content'))) \
    .withColumn('content', regexp_replace(col('content'),money_regex,'normalized_currency'))
    '''
    from there, we just need to get rid of all the special chars and
    stuff so we can just have words.
    '''
    raw_data.show(5)
    spam_clean_data = raw_data.filter(raw_data.classified == 'spam')
    ham_clean_data = raw_data.filter(raw_data.classified == 'ham')
    ham_clean_data.show(5)
    '''
    next we just need to make the words into something we can work
    with... easy just the word and its count
    '''


    

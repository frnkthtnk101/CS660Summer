from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType, StructField, StructType
from os import path
sc = SparkContext("local", "spam_to_ham")
spark = SparkSession.builder.getOrCreate()
home = "/Users/francopettigrosso/ws/CS660Summer/samples/"
trained_data = home+"trained_data.csv"
training_data = home+"training_data.csv"
input_text = home+"sentences.txt"
words = r"([a-z|A-Z]+)"
stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 
   'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for',
   'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 
   'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 
   'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 
   'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 
   'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
   'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not',
   'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which',
   'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by',
   'doing', 'it', 'how', 'further', 'was', 'here', 'than' ]


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
    raw_data = raw_data.withColumn('content', lower(col('content')))
    raw_data = raw_data.withColumn('content', split(col('content'),' '))
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
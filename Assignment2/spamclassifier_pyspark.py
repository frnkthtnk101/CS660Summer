from pyspark.sql import  *
from pyspark.sql.functions import *
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from re

STOP_WORDS = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 
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

DIRTY_FILE_PATH = '/Users/francopettigrosso/ws/CS660Summer/samples/spam.csv'
SCRUBBED_FILE_PATH = '/Users/francopettigrosso/ws/CS660Summer/samples/spam_scrubbed.csv'
cleaned_lines= []
with file_read as open(DIRTY_FILE_PATH,'r'):
    with file_write as open(SCRUBBED_FILE_PATH,'w'):
        for line in file_read:
            split_words = line.split()
            no_stop_words = [word for word in split_words if word.lower() not in STOP_WORDS]
            cleaned_lines.append(' '.join(no_stop_words))
        file_write.writelines(cleaned_lines)

#create session
spark = SparkSession.builder.getOrCreate()
# Read csv
df = spark.read.csv('', header = True )
df=df.select(df.columns[:2])

#### Transformation and cleaning
df2=df.withColumnRenamed('v1','target').withColumnRenamed('v2','email')

# Convert target column to numeric
df2=df2.withColumn('target',when(df2.target=='spam',1).otherwise(0))\
.withColumn('split_email',split(df2['email'], ' ')).orderBy('target',ascending=False)
# Remove null values
df2=df2.where(~df2.email.isNull())

# Convert target to stringindex
label_stringIdx = StringIndexer(inputCol="target", outputCol="label",stringOrderType="alphabetDesc")
df2_new=label_stringIdx.fit(df2).transform(df2)

# Fectorize words
hashingTF = HashingTF(inputCol="split_email", outputCol="rawFeatures", numFeatures=100)
featurizedData = hashingTF.transform(df2_new)


# Split train and test data
[training_data, test_data] = featurizedData.randomSplit([0.8, 0.2])
training_data.cache()
test_data.cache()


# Naive Bayes
nb = NaiveBayes(smoothing=1.0,featuresCol='rawFeatures', labelCol='label',modelType='multinomial')
# train the model
model = nb.fit(training_data)
# select example rows to display.
predictions = model.transform(test_data)

# Evaluate with ROC
evaluator = BinaryClassificationEvaluator(labelCol="label")
print('Test Area Under ROC', evaluator.evaluate(predictions))


# Print out confusion matrix
predictions.crosstab('target','prediction').show()
'''
+-----------------+---+---+
|target_prediction|0.0|1.0|
+-----------------+---+---+
|                1| 73| 54|
|                0| 19|940|
+-----------------+---+---+
'''

# Random forest
# Create an initial RandomForest model.
rf = RandomForestClassifier(labelCol="label", featuresCol="rawFeatures",numTrees=10)

# Train model with Training Data
rfModel = rf.fit(training_data)


evaluator = BinaryClassificationEvaluator(labelCol="label")
print('Test Area Under ROC', evaluator.evaluate(predictions))

predictions2=rfModel.transform(test_data)


### Evaluating the model
evaluator = BinaryClassificationEvaluator(labelCol="label")
print('Test Area Under ROC', evaluator.evaluate(predictions2))
#0.92
# Print out confusion matrix
predictions2.crosstab('target','prediction').show()
'''
+-----------------+---+---+
|target_prediction|0.0|1.0|
+-----------------+---+---+
|                1|  7|140|
|                0|  0|940|
+-----------------+---+---+
'''
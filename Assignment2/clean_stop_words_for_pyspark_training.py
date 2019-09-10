'''
clean_stop_words_for_pyspark_training.py
franco john eric tod
'''
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
file_read = open(DIRTY_FILE_PATH, 'r', encoding="ISO-8859-1")
file_write = open(SCRUBBED_FILE_PATH, 'w', encoding="ISO-8859-1")
for line in file_read:
   split_words = line.lower().split(',',1)
   no_stop_words = [word for word in split_words[1].split() if word not in STOP_WORDS]
   cleaned_lines.append(split_words[0] + ','+ ' '.join(no_stop_words))
file_write.write('\r\n'.join(cleaned_lines))
file_read.close()
file_write.close()
#the website is http://www.gutenberg.org/files/59812/59812-0.txt
#download ideas came from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3

import urllib.request

# when everything works according to plan (no 404)
'''url = 'http://www.gutenberg.org/files/59812/59812-0.txt'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
print(text)
'''

# when we get a 404
'''url = 'http://www.gutenberg.org/files/2/2-0.txt'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
print(text)'''
#urllib.error.HTTPError: HTTP Error 404: Not Found
PATH = 'C:\\BTBTestArea\\BTB test area\\FTP\\'

def Main():
    for i in range (1,1000):
        url = f'http://www.gutenberg.org/files/{i}/{i}-0.txt'
        try:
            response = urllib.request.urlopen(url)
            data = response.read()      # a `bytes` object
            text = data.decode('utf-8-sig')
            book = open(f'{PATH}book{i}.txt','w',encoding = 'utf-8-sig')
            book.write(text)
            book.close()
        except Exception as e:
            print(e)
        
Main()
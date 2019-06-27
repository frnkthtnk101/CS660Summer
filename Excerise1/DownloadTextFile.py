#the website is http://www.gutenberg.org/files/59812/59812-0.txt
#download ideas came from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3

import urllib.request
...
url = 'http://www.gutenberg.org/files/59812/59812-0.txt'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is bina
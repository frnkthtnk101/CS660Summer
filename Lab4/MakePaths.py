from os import listdir
from os.path import isfile, join

mypath = '/Users/francopettigrosso/ws/CS660Summer/samples'
out = '/Users/francopettigrosso/ws/CS660Summer/samples/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
t = open(f'{mypath}/files.txt','w')
for i in onlyfiles:
    t.write(f'{out}{i}\r\n')
t.close()
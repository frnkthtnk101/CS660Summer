#geeks for geeks
# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 

def simple_function(x):
    return list(x)

def map(funct, ite):
    for i in ite:
        yield funct(i)

for i in map(simple_function, l):
    print(i)

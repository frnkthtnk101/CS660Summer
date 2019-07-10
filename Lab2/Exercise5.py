#exercise5
#generate a map using a generator
#franco

def square(x):
    return x * x
a_generator_in_a_cool_way = [square(x) for x in range(1,20)] #generator
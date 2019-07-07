def square(x):
    return x * x


a_map = map(square, range(1,20))
a_list = list(map(square, range(1,20)))
a_lambda_map = map(lambda x: x * x, range(1,20))

#for index in a_lambda_map:
#    print(index)

a_generator_in_a_cool_way = [square(x) for x in range(1,20)] #generator
a_list_in_a_cool_way = (square(x) for x in range(1,20)) #list
is_even_generator = filter(lambda x : x % 2 == 0, a_generator_in_a_cool_way)

for index in is_even_generator:
    print(index)


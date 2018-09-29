# Homework 3
# Hashvel listi meji bolor parz tveri gumar@:
# ham karch kam map, reduce, filter functianerov
from functools import reduce


def prime_numbers_list(n):
    lst = list(range(n))
    sqr = len(lst) ** 0.5 + 1

    for i in lst:
        if i > len(lst) ** 0.5:
            break
        if i in [-1, 0, 1] or i > sqr:
            continue
        for j in range(2 * i, len(lst), i):
            lst[j] = -1

    lst = [i for i in lst if lst[i] not in [-1, 0, 1]]
    return lst


print(prime_numbers_list(100))


def func1(x, y):
    return x + y


def func2(x):
    if x % 2 == 0:
        return x


def func3(x):
    return x ** 2


prime_list = prime_numbers_list(100)
# Reduce function!
sum_of_prime_numbers1 = reduce(func1, prime_list)  # Why 0 is not passed through function but in lambda function passed?
sum_of_prime_numbers2 = reduce(lambda x, y: x + y, prime_list)
print(f'sum_of_prime_numbers1 = {sum_of_prime_numbers1}')
print(f'sum_of_prime_numbers2 = {sum_of_prime_numbers2}')

# Filter function!
even_prime_numbers1 = list(filter(func2, prime_list))
even_prime_numbers2 = list(filter(lambda x: x % 2 == 0, prime_list))
print(f'even_prime_numbers1 = {even_prime_numbers1}')
print(f'even_prime_numbers2 = {even_prime_numbers2}')

# Map function!
squares_of_prime_numbers1 = list(map(lambda x: x ** 2, prime_list))
squares_of_prime_numbers2 = list(map(func3, prime_list))
print(f'squares_of_prime_numbers1 = {squares_of_prime_numbers1}')
print(f'squares_of_prime_numbers2 = {squares_of_prime_numbers2}')


lst1 = list(range(0, 10))
print("\n")
print(lst1)

# Reduce function!
value1 = reduce(func1, lst1)     # Why 0 is not passed through function but in lambda function passed?
value2 = reduce(lambda x, y: x + y, lst1)
print(f'value1 = {value1}')
print(f'value2 = {value2}')

# Filter function!
value3 = list(filter(func2, lst1))
value4 = list(filter(lambda x: x % 2 == 0, lst1))
print(f'value3 = {value3}')
print(f'value4 = {value4}')

# Map function!
value5 = list(map(lambda x: x ** 2, lst1))
value6 = list(map(func3, lst1))
print(f'value5 = {value5}')
print(f'value6 = {value6}')

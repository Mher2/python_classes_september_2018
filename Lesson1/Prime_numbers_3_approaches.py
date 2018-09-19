import timeit


def approach1(given_number):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, given_number + 1):
        # Assume number is prime until shown it is not.
        is_prime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                is_prime = False
        if is_prime:
            primes.append(possiblePrime)

    return primes


def approach2(given_number):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, given_number + 1):
        # Assume number is prime until shown it is not.
        is_prime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possiblePrime)


def approach3(given_number):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, given_number + 1):
        # Assume number is prime until shown it is not.
        is_prime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possiblePrime)

    return primes


def approach4(n):
    # n = 25
    lst = list(range(n))

    sqr = len(lst) ** 0.5 + 1
    # print(sqr)

    for i in lst:
        if i > len(lst) ** 0.5:
            break
        if i in [-1, 0, 1] or i > sqr:
            continue
        for j in range(2 * i, len(lst), i):
            lst[j] = -1

    return lst


# Approach 1: Execution time
# print(timeit.timeit('approach1(500)', globals=globals(), number=10000))
# Approach 2: Execution time
print(timeit.timeit('approach2(500)', globals=globals(), number=1000))

# Approach 3: Execution time
print(timeit.timeit('approach3(500)', globals=globals(), number=1000))

# Approach 4: Execution time
print(timeit.timeit('approach4(500)', globals=globals(), number=1000))

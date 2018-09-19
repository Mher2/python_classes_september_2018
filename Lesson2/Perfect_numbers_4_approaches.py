import timeit


def perfect_numbers_1(n):
    """
    My Approach 1
    :param n:
    :return:
    """
    perfect_numbers = []
    for i in range(2, n):
        s = 0
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                s = s + j
        if i == s + 1:
            perfect_numbers.append(i)
    return perfect_numbers


def perfect_numbers_2(n):
    """
    Bad not my Approach 2
    :param n:
    :return:
    """
    perfect_numbers2 = []
    for i in range(2, n):
        s = 0
        for j in range(2, i):
            if i % j == 0:
                s = s + j
                # print(f'i = {i}, j = {j}, s = {s}')
        # if i in range(10000, n, 10000):
            # print(f'i={i}')
        if i == s+1:
            perfect_numbers2.append(i)
    return perfect_numbers2


def perfect_numbers_3(k):
    """
    Not my Approach 3
    :param k:
    :return:
    """
    x = []
    n = 1
    while n < k:
        if sum([i for i in range(1, n) if n % i == 0]) == n:
            x.append(n)
        n += 1
    return x


def perfect_numbers_4(k):
    """
    Not my Approach 4
    :param k:
    :return:
    """
    arr = []
    for c in range(2, k):
        if sum(x for x in range(1, int(c/2)+1) if not c % x) == c:
            arr.append(c)
    return arr


print(perfect_numbers_1(1000))
print(perfect_numbers_2(1000))
print(perfect_numbers_3(1000))
print(perfect_numbers_4(1000))

# exit(0)

# Approach 1: Execution time    200 - 3.766         0.37
print(timeit.timeit('perfect_numbers_1(200)', globals=globals(), number=1000))

# Approach 2: Execution time    200 - 6.476         0.64
print(timeit.timeit('perfect_numbers_2(200)', globals=globals(), number=1000))

# Approach 3: Execution time    200 - 7.03          0.71
print(timeit.timeit('perfect_numbers_3(200)', globals=globals(), number=1000))

# Approach 4: Execution time
print(timeit.timeit('perfect_numbers_4(200)', globals=globals(), number=1000))

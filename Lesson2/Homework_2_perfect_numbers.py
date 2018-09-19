n = 10000

perfect_numbers = []
for i in range(2, n):
    s = 0
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            s = s + j
    if i == s + 1:
        perfect_numbers.append(i)

print(perfect_numbers)

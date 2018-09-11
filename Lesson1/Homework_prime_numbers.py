numbers_list = [181, 1, 259, 5, 7, 170, -8, 120, 131]
prime_numbers_list = []

for number in numbers_list:
    print("Checking item: " + str(number))
    is_prime_number = True
    divisible_list = []

    if number > 2:
        for i in range(2, int(number ** 0.5) + 1):   # Approach 3 is Much more faster
            is_divisible = True
            if i not in divisible_list:
                for j in divisible_list:
                    if i % j == 0:
                        is_divisible = False
                        break
                if is_divisible:
                    divisible_list.append(i)
                    print(str(number) + " % " + str(i) + " = " + str(number % i))
            if number % i == 0:
                is_prime_number = False
                break

    print("divisibles: " + str(divisible_list))
    if is_prime_number and number > 1:
        print("Item " + str(number) + " is prime.")
        prime_numbers_list.append(number)

    else:
        print("Item " + str(number) + " is not prime.")
    print("---")

print("Numbers list is: " + str(numbers_list))
print("Prime numbers list is: " + str(prime_numbers_list))

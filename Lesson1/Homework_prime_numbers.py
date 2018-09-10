numbers_list = [18, 1, 2, 5, 7, 17, -8, 12, 13]
prime_numbers_list = []

for number in numbers_list:
    is_prime_number = True
    if number > 2:

        # print(int(number ** 0.5) + 1)
        # for i in range(2, int(number ** 0.5) + 1):    Approach 2 is Faster

        for i in range(2, number):  # Approach 1
            print(str(number) + " % " + str(i) + " = " + str(number % i))

            if number % i == 0:
                is_prime_number = False
                break

    if is_prime_number and number > 1:
        print("Item " + str(number) + " is prime.")
        prime_numbers_list.append(number)
        print("---")

print("Numbers list is: " + str(numbers_list))
print("Prime numbers list is: " + str(prime_numbers_list))

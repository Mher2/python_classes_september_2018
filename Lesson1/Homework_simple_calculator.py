first_num = int(input("Input first number: "))
second_num = int(input("Input second number: "))
action = str(input("Input one of the actions addition(+), subtraction(-), multiplication(*), division(/) "
                   "or \"exit\" to exit: "))

while action != "exit":

    if action == "+":
        print(str(first_num) + " + " + str(second_num) + " = " + str(first_num + second_num))
    elif action == "-":
        print(str(first_num) + " - " + str(second_num) + " = " + str(first_num - second_num))
    elif action == "*":
        print(str(first_num) + " * " + str(second_num) + " = " + str(first_num * second_num))
    elif action == "/":
        print(str(first_num) + " / " + str(second_num) + " = " + str(first_num / second_num))
    else:
        print("Your input is: \"" + str(action) + "\" it is not one of following actions +, -, *, /.\nExiting...")

    first_num = int(input("Input first number: "))
    second_num = int(input("Input second number: "))
    action = str(input("Input one of the actions addition(+), subtraction(-), multiplication(*), division(/) "
                       "or \"e\" to exit: "))

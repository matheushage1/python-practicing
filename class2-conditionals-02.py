first_value = input("Type the first value: ")
second_value = input("Type the second value: ")

if int (first_value > second_value):
    print("The first value is bigger than the second value")
elif first_value < second_value:
    print("The first value is lower than the second value")
elif first_value == second_value:
    print("Both are the same.")
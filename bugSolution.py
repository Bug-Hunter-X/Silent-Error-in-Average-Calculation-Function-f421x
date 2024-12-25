def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return None # Return None to explicitly indicate an empty list
    average = total / count
    return average

my_list = []
average = calculate_average(my_list)
if average is None:
    print("Input list is empty.")
else:
    print(f"The average is: {average}")

my_list = [10, 20, 30]
average = calculate_average(my_list)
if average is None:
    print("Input list is empty.")
else:
    print(f"The average is: {average}") 
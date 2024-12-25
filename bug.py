def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    average = total / count
    return average

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 0

my_list = [10, 20, 30]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 20.0
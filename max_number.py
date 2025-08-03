# Your Task

# Define a function called find_max that accepts a list of integers or floats.
# Return the largest number in the list.
# Do not use the built-in max() function — try to solve it manually using:
# A for loop to check each number
# # A variable to track the current maximum
import random

numbers = []
for _ in range(100):
    if random.choice([True, False]):
        numbers.append(random.randint(1,5000))
    else:
        numbers.append(random.uniform(1,5000))

def find_max(numbers: list[int | float]):
    max_so_far = numbers[0]
    for n in numbers:
        if n > max_so_far:
            max_so_far = n
    return max_so_far

print(find_max(numbers))
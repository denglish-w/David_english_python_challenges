# Your Task

# Define a function called is_prime that takes one integer as input.
# Return True if the number is prime and False otherwise.
# Use a loop to check divisibility — don’t use any external libraries or built-in prime checkers.
# Concepts Tested

# Conditional logic
# Loops
# Modulo operator (%)
# Efficiency and edge case handling
# Stretch Ideas

# Improve performance by only looping up to the square root of the number
# Write a second function that returns all prime numbers up to a given number
# Accept user input and check multiple numbers in one run
# Save all prime results to a file
# Hints:

# Any number less than 2 is not prime.
# Use % to check for divisibility.
# If any number between 2 and n-1 divides evenly into n, it’s not prime.

def is_prime(num: int):
    n = int(input("Please input an integer "))
    if num < 2:
        return False
    for n in range(2, n-1):
        if n % 2 == 0:
            return False
        else:
            return True


        
    
# our Task

# Define a function called is_palindrome that accepts a single string.
# Return True if the string is a palindrome, and False otherwise.
# Normalize the string by:
# Converting it to lowercase
# Removing spaces (and optionally punctuation)
# Reverse the normalized string and compare it to the original normalized version.

def is_palindrome(p):
   p = p.lower().replace(" ", "")
   return p[::-1] == p

word = input('Check if you word is a palindrome ')

print(is_palindrome(word))
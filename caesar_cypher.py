# Define a function called caesar_cipher that accepts:
# a string text
# an integer shift
# Return a new string with each alphabetical character shifted by the shift amount.
# Keep the case (uppercase/lowercase) the same.
# Do not change non-letter characters like punctuation, spaces, or numbers.
# Concepts Tested

# String manipulation
# Character encoding with ord() and chr()
# Modulo math for wrapping the alphabet
# Control flow and logic

def caesar_cypher(cypher: str, shift: int):
    cypher_list = list(cypher)
    
    for letter in cypher_list:
        unicode_number = ord(letter)
        if unicode_number in range(65, 91):
            uppercase_index = (unicode_number - 65)
            shifted_upper_index = (((uppercase_index + shift) % 26) + 65)
            print(chr(shifted_upper_index), end="")
        elif unicode_number in range(97, 123):
            lowercase_index = (unicode_number - 97)
            shifted_lower_index = (((lowercase_index + shift) % 26) + 97)
            print(chr(shifted_lower_index), end="")
        else: 
            print(letter, end="")
    print()
    
caesar_cypher(input("Type your string here: "), int(input("And your number here ")))
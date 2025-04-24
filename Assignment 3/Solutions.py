"""
Solutions to assignment 3
"""

"""

"""
string = "Programming"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)



"""

"""
full_name = input("Enter your full name: ")
name_parts = full_name.split()initials = ""
for part in name_parts:
    initials += part[0].upper() + "."
print(initials)


def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Input string from the user
input_string = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")




4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

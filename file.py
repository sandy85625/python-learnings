import string

'''
Write a python program to
a) read user input and write to a file
b) read the file and print the number of lines, words, alphabets, digits, white spaces, and special characters in the file
Handle all possible exceptions.
'''

# Define a function to count the number of lines, words, characters, and digits in a string
def count_file_stats(contents):
    lines = contents.count('\n')
    words = len(contents.split())
    chars = len(contents)
    digits = sum(c.isdigit() for c in contents)
    spaces = sum(c.isspace() for c in contents)
    specials = sum(c in string.punctuation for c in contents)
    
    return lines, words, chars, digits, spaces, specials

try:

    print("==========================================")
    print("Writing to a File and Get File Statistics")
    print("==========================================")
    # Read user input and write it to a file
    filename = input("\nEnter a filename to write to: ")
    with open(filename, 'w') as file:
        user_input = input("\nEnter some text to write to the file: ")
        file.write(user_input)

    # Read the file and count the statistics
    with open(filename, 'r') as file:
        contents = file.read()
        lines, words, chars, digits, spaces, specials = count_file_stats(contents)

    # Print the statistics
    print("------------------------------")
    print("File statistics:")
    print("\nLines:", lines)
    print("Words:", words)
    print("Characters:", chars)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Special characters:", specials)
    
except Exception as e:
    print("An error occurred:", str(e))

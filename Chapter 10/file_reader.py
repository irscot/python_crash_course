# The open function opens the file with file's name.
# Keyword with closes the file once access is no longer needed.
# We've already accessed once and once is enough.

with open('pi_digits.txt') as file_object:
    # Use the read method to read the file and store in variable contents.
    contents = file_object.read()
print(contents)
# If working with a file within a folder:
# Use with open('text_files/filename.txt') as file_object:
# Windows systems use a backslash (\) instead of a forward slash (/) when displaying
# file paths, but you can still use forward slashes in your code.


# If you try to use backslashes in a file path, you’ll get an error because the backslash is
# used to escape characters in strings. For example, in the path "C:\path\to\file.txt",
# the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape
# each one in the path, like this: "C:\\path\\to\\file.txt".

# Reading Line by Line.
print("\nLet's read it line by line:")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

print("\nNow let's use rstrip() to take out the extra blank lines")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a file.
print("\nLet's store each line in a list:")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # readlines() method takes each line and stores it in a list.
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Is Your Birthday Contained in Pi?
print("\nDoes my birthday show up in pi?")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # readlines() method takes each line and stores it in a list.
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
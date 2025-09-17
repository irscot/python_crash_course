# Writing a File

filename = 'programming.txt'
# 'w', tells Python that we want to open the file in write mode.
# Be careful opening a file in write mode ('w') because if the file does exist,
# python will erase the contents of the file before returning the file object.


# read mode ('r'), write mode ('w'), append mode ('a').
# a mode that allows you to read and write to the file ('r+').
# The open() function automatically creates the file you’re writing to if it doesn't exist.
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love making games.\n")

# Appending to a File
# Appended text will be written at the end of the file.
with open(filename, 'a') as file_object:
    file_object.write("I love making apps that help others.")

# This program doesn't have a terminal out put.
# But if you open the file programming.txt you'll see the line we wrote.
# Run the program and the txt file will be made with these lines written here.

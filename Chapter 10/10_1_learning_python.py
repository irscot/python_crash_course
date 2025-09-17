# Make text file what_ive_learned.txt and read it here in three different ways.
filename = 'what_ive_learned.txt'
# Print the contents of the text file by:

# 1 - Reading the entire file.
with open(filename) as file:
    python = file.read()
print(python)

# 2 - By looping over the file object's line by line.
print("\n")
with open(filename) as file:
    for line in file:
        print(line.rstrip())

# 3 - By starting the lines in a list and then working with them outside the with block.
print("\n")
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())

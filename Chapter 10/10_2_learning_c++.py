# Use the replace() method to change python to C++ in what_ive_learned.txt
filename = 'what_ive_learned.txt'

# Change python to C++ in each line.
# First use the readlines() method after the with line of code
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C++'))

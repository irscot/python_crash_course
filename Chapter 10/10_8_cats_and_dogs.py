# Make two files called cats.txt and dogs.txt.
# Store 3 names in each file.

# Write a program that tries to rad these files and print the contents of the files.
filenames = ['bears.txt', 'cats.txt', 'dogs.txt', 'deer.txt']

for filename in filenames:
    print(f"\nPlease wait...\nReading {filename}...")

    try:
        with open(filename) as f:
            read_file = f.read()
            print(read_file)
    except FileNotFoundError:
        print("Sorry I can't find the file.")

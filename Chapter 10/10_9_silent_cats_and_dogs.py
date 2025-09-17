# Modify the except block from 10_8_cats_and_dogs.py
# to fail silently if any of the files are missing.

filenames = ['bears.txt', 'cats.txt', 'dogs.txt', 'deer.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            read_file = f.read()
    # If it has a FileNotFoundError then use except to pass that error.
    # That way bears.txt and deer.txt doesn't show up when the program is run.
    except FileNotFoundError:
        pass
    # Move the print(f"\nPlease wait...\nReading {filename}...") and
    # print(read_file) part to else,
    # so that it only runs when there is no file errors
    else:
        print(f"\nPlease wait...\nReading {filename}...")
        print(read_file)

filename = 'guest_book.txt'

print("\nType 'quit' to stop the program.")

# Write a while-loop that prompts users for their name.
while True:
    name = input("\nWhat is your name? ")

# When they enter their name, print a greeting.
    print(f"Hello, {name.title()}")
    if name == 'quit':
        print("See ya later!")
        break
    else:
        # Add a line recording their visit in a file called guest_book.txt.
        # Make sure each line appears on a new line.
        with open(filename, 'r+') as file_object:
            file_object.write("Guest Book: \n")
        with open(filename, 'a') as file_object:
            file_object.write(f"- {name.title()}\n")
        print(f"Hope you enjoy your visit, {name.title()}.\n")

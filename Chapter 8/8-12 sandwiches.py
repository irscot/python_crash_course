# Write a function that accepts a list of items on a sandwich.
items = ['bacon']

def make_sandwich(*items):
    print("Here's what they want on the sandwich: ")
    for item in items:
        print(f"\t-{item}")


make_sandwich('bacon', 'cheese')
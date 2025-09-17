# Write function make_shirt() with size
# and text (what will be printed on the shirt) as parameters.
def make_shirt(size, text):
    print(f"We will make a {size} shirt that says '{text}'.")

# Call function with:

# Position arguments.
print("Postion Arguments style ('small', 'Dont look at me like that')")
make_shirt('small', 'Dont look at me like that')

# Keyword arguments.
print("\nKeyword Arguments style (size='small', text='Dont look at me like that')")
make_shirt(size='small', text='Dont look at me like that')

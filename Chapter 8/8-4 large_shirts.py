# Modify the make_shirts function so the size is set large as the default.

def make_shirt(text='I love Python', size='large'):
    """"Tell them what their shirt will say"""
    print(f"\nYour {size} shirt will say '{text}'.")


# Statement with defaults
make_shirt()

# Statement with a change in size default.
make_shirt(size='extra-large')

# Statement with a change in size and text defaults.
make_shirt(size='medium', text='Anime is Trash')

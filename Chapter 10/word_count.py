def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        # When you want the error message to fail silently use the following:
        # pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['what_ive_learned.txt', 'why_we_like_programming.txt']
for filename in filenames:
    count_words(filename)

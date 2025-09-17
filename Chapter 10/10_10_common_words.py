# Visit Project Gutenberg and find a few texts to analyze.
# Download them or copy the text from the browser into a txt file.
# Use the count() method to find out how many times a word show up.

def count_words_in_common(filename, word):
    """Count how many times a word shows up in the text files."""
    try:
        with open(filename, encoding='utf-8') as f:
            read_file = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = read_file.lower().count(word)

        details = f"The word '{word}' shows up in {filename} about {word_count} times."
        print(details)


# Let's see how many times その時 shows up in the america_monogatari.txt file.
filename = 'america_monogatari.txt'
count_words_in_common(filename, 'その時')

# Dictionaries work in a key-value pair.
# Make a glossary of 5 programming words.
# Key is the term and value is the meaning.

glossary = {'tuple': 'like a list but cannot change.',
            'dictionary': 'a key-value list.',
            'if statement': 'statement that checks for conditions.',
            'variable': 'a piece info that is given a value.',
            'loops': 'a system that allows you to repeat code.'}

# Print each word and it's meaning. Use a for loop to go through all terms.
# term is assigned to the key while the meaning is assigned to the value.
for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}\n")

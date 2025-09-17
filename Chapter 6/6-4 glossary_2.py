# Dictionaries work in a key-value pair 'key': 'value',.
# Make a glossary of 5 programming words.
# Key is the term and value is the meaning.

# I'll make a japanese dictionary instead of adding terms to 6-3

JP_glossary = {'暗号': 'cipher', '探偵': 'detective', 'リンゴ': 'apple',
            '扉': 'door', '本': 'book', 'えんぴつ': 'pencil', '夜': 'night',
            '心臓': 'heart', '米': 'rice', '写真': 'photo'}


for japanese_word, english_word in JP_glossary.items():
    print(f"The Japanese word {japanese_word} means {english_word.title()} in English.")
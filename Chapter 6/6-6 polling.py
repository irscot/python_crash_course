# Make a list of people who should take the favorite languages poll.

favorite_languages = {'michael': 'python',
                      'elma': 'java',
                      'phil': 'c++',
                      'sarah': 'html',
                      'isiah': 'python',
                      'edward': 'c#'}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print(f"\n")
# If their name shows up in favorite_languages and programmers then
# they will receive  a thank-you message.
# If they don't show up in favorite languages (like asuka and angelo),
# they will be sent a message asking them what is their favorite programming language.

programmers = ['elma', 'isiah', 'sarah', 'michael', 'angelo', 'asuka']


# Loop through list of people who should take the poll.
# If they've already taken it, print a thank-you message.
for programmer in programmers:
    if programmer in favorite_languages.keys():
        print(f"Thank you {programmer.title()} for taking the poll.")
    # If they haven't, print a messages asking them to take the poll.
    else:
        print(f"{programmer.title()}, do you have a favorite programming language?")

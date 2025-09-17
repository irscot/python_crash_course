# Tests for equality and inequality with strings
name = 'isiah'
print(name)


print("\nDoes name == 'isiah'?")
name == 'isiah'
print(name == 'isiah')


print("\nDoes name == 'Isiah'?")
name == 'Isiah'
print(name == 'Isiah')

print("\nDoes name != 'Isiah'?")
name != 'Isiah'
print(name != 'Isiah')



# Tests using the lower() method
name = 'Sakura'
print(name)

print("\nDoes name == 'sakura'?")
name.lower() == 'sakura'
print(name.lower() == 'sakura')


# Numerical tests for equality and inequality
pi = 3.14
print(f"\nWhat is pi with two decimal places (Ex: 0.00)?")
if pi == 3.14:
    print("Yes pi is 3.14. But it's a longer story than that.")

if pi != 3.14:
    print("That's not quite right.")

# Greater than or less than or equal to
age = 20
age_to_drink = 21
if age >= age_to_drink:
    print("\nWhat would you like to drink?")
else:
    print("\nCome back when you're old enough to drink.")

if age < age_to_drink:
    print("\nYou're not old enough to drink.")

# Test using and
voice_actresses = ['Hasami Saori', 'Kitou Akari', 'Taketatsu Ayane']
voice_actor = ['J. Michael Tatum']
print("\nAre they voice actresses?")
print(voice_actresses == 'Hasami Saori' and voice_actor == 'J. Michael Tatum')


# Test using or
number_0 = 0
number_1 = 1

print(f"\nIs {number_0} bigger than {number_1}?")
print(number_0 >= number_1 or number_0 > 1)

# Test if item is in list
voice_actresses = ['Hasami Saori', 'Kitou Akari', 'Taketatsu Ayane']
print("\nIs Hasami Saori a voice actress?")
print('Hasami Saori' in voice_actresses)

# Test if item is not in list
japanese_writing = ['hiragana', 'katakana', 'kanji']
print("\nIs hangul a type of Japanese writing?")
print('hangul' in japanese_writing)


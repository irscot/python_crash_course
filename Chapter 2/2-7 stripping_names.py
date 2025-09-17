#Use a variable to represent a person’s name, and include
#some whitespace characters at the beginning and end of the name. Make sure
#you use each character combination, "\t" and "\n", at least once.

name = ' Isiah '
name_tab = ' \tIsiah '
name_new_line = ' \nIsiah\n '

print(name)
print(name_tab)
print(name_new_line)


#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip().
print("Unchanged:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())




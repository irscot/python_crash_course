#Make a list of languages you are literate in.

literate_langauages = ['Japanese', 'English']

print("Here is the list in alphabetical order:")
print(sorted(literate_langauages))
print(f"\nHere is the original list again:\n {literate_langauages}\n")

#Use reverse(). Print reversed list.

literate_langauages.reverse()
print(f"Here is the reversed list:\n {literate_langauages}")

#change it back to the original and print.
print("\nChanging the list back to the original:")
literate_langauages.reverse()
print(literate_langauages)

#Use sort() to put list in a permanent alphabetical order.
literate_langauages.sort()
print(f"\nHere is the permanent alphabetical list: \n{literate_langauages}")

#Use sort() to change list to reverse alphabetical order.
print("\n Here is the reverse alphabetical order:")
literate_langauages.sort(reverse=True)
print(literate_langauages)
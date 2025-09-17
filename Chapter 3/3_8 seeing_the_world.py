#Make a list of 5 places you'd like to go.

#Store the locations in a list and print.

travel_to = ['Hokkaido', 'Akihabara', 'Okinawa', 'Kyushu', 'Gunma']
print(f"Here is the original list:\n {travel_to}\n")

#Use sorted() to put list in alphabetical order and print it.
#This will not change the order of the original.
#Show that the original list is not effected.
print("Here is the list in alphabetical order:")
print(sorted(travel_to))
print(f"\nHere is the original list again:\n {travel_to}\n")

#Use reverse(). Print reversed list.

travel_to.reverse()
print(f"Here is the reversed list:\n {travel_to}")

#change it back to the original and print.
print("\nChanging the list back to the original:")
travel_to.reverse()
print(travel_to)

#Use sort() to put list in a permanent alphabetical order.
travel_to.sort()
print(f"\nHere is the permanent alphabetical list: \n{travel_to}")

#Use sort() to change list to reverse alphabetical order.
print("\n Here is the reverse alphabetical order:")
travel_to.sort(reverse=True)
print(travel_to)
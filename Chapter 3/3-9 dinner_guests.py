#Work with 3-4 and use len() to print a message to indicate how many people
# are invited for dinner

guest_list = ['青山せんせい', 'conan doyle', '新保せんせい']

guest_message_a = f"こんばんは, {guest_list[0]}, 一緒に晩御飯しませんか。"
print(guest_message_a)

guest_message_cd = f"Good evening, {guest_list[1]}, would you like to have dinner?"
print(guest_message_cd)

guest_message_s = f"こんばんは, {guest_list[2]}, 一緒に晩御飯しませんか。"
print(guest_message_s)

print(len(guest_list))
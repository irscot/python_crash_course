#Aoyama couldn't make it to the dinner. Invite someone else.

guest_list = ['青山せんせい', 'conan doyle', '新保せんせい']

guest_message_a = f"こんばんは, {guest_list[0]}, 一緒に晩御飯しませんか。"
print(guest_message_a)

guest_message_cd = f"Good evening, {guest_list[1]}, would you like to have dinner?"
print(guest_message_cd)

guest_message_s = f"こんばんは, {guest_list[2]}, 一緒に晩御飯しませんか。"
print(guest_message_s)

#Remove Aoyama from the guest list and invite nisiOisin instead.
cant_make_it = f"{guest_list[0]} can't make it to the dinner. I'll invite nisiOisin."
print(cant_make_it)

guest_list.remove('青山せんせい')
print(guest_list)

guest_list.insert(0, 'nisiOisin')
print(guest_list)

#New Invitations
guest_message_n = f"こんばんは, {guest_list[0]}, 一緒に晩御飯しませんか。"
print(guest_message_n)

guest_message_cd = f"Good evening, {guest_list[1]}, would you like to have dinner?"
print(guest_message_cd)

guest_message_s = f"こんばんは, {guest_list[2]}, 一緒に晩御飯しませんか。"
print(guest_message_s)
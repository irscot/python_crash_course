#New table won't be here in time. Can only invite two guests T_T.

guest_list = ['nisiOisin', 'conan doyle', '新保せんせい']

guest_message_0 = f"こんばんは, {guest_list[0]}, 一緒に晩御飯しませんか。"
print(guest_message_0)

guest_message_1 = f"Good evening, {guest_list[1]}, would you like to have dinner?"
print(guest_message_1)

guest_message_2 = f"こんばんは, {guest_list[2]}, 一緒に晩御飯しませんか。"
print(guest_message_2)

update_message = f"Found a bigger table!\b"
print(update_message)

guest_list.insert(3, 'Joey')
guest_list.insert(4, 'Garnt')
guest_list.insert(5, 'Connor')

guest_message_0 = f"こんばんは, {guest_list[0]}, 一緒に晩御飯しませんか。"
print(guest_message_0)

guest_message_1 = f"Good evening, {guest_list[1]}, would you like to have dinner?"
print(guest_message_1)

guest_message_2 = f"こんばんは, {guest_list[2]}, 一緒に晩御飯しませんか。"
print(guest_message_2)

guest_message_3 = f"Good evening, {guest_list[3]}, would you like to have dinner?"
print(guest_message_3)

guest_message_4 = f"Good evening, {guest_list[4]}, would you like to have dinner?"
print(guest_message_4)

guest_message_5 = f"Good evening, {guest_list[5]}, would you like to have dinner?"
print(guest_message_5)

bad_news_message = "Table won't be here in time for dinner so I can only invite two guests."
print(bad_news_message)
print(guest_list)


sorry_doyle = f"Sorry, {guest_list[1]}, we can have dinner when I get a bigger table."
print(sorry_doyle)
guest_list.pop(1)
print(guest_list)

sorry_joey = f"Sorry, {guest_list[2]}, we can have dinner when I get a bigger table."
print(sorry_joey)
guest_list.pop(2)
print(guest_list)

sorry_garnt = f"Sorry, {guest_list[2]}, we can have dinner when I get a bigger table."
print(sorry_garnt)
guest_list.pop(2)
print(guest_list)

sorry_garnt = f"Sorry, {guest_list[2]}, we can have dinner when I get a bigger table."
print(sorry_garnt)
guest_list.pop(2)
print(guest_list)

still_invite_nisiOisin = f"{guest_list[0]}, まだ一緒に晩ご飯を食べませんか？"
print(still_invite_nisiOisin)

still_invite_shinbo = f"{guest_list[1]}, まだ一緒に晩ご飯を食べませんか？"
print(still_invite_shinbo)

#Time to delete last two guests from list. Thus clearing the list completely.

del guest_list[0]
del guest_list[1]
print(guest_list)



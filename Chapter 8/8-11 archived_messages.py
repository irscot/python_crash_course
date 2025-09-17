# Start with 8-10 sending_messages.py
# Call the function send_messages() with a copy of the text messages
# while it is being printed.

txts = ['yo', 'hiya', 'what up tho fam', 'yahallo']
sent_txts = []


# Pass the list to a function called show_messages() that prints the texts.
# To keep it more organized,
# need one function that appends (send_messages) the list
# and another to show the texts (show_messages).

def send_messages(txts, sent_txts):
    """Move each text to sent_txts list"""
    # Need a while loop to remove (pop) txts list values
    # and add (append) to sent_txts list.
    while txts:
        sending_txt = txts.pop()
        print(f"Sending text: {sending_txt}")
        sent_txts.append(sending_txt)



def show_messages(sent_txts):
    """Shows each text in sent_txts list"""
    print("\nHere are the sent text messages: ")
    # Use this for loop to print off each text messages within the list.
    for sent_txt in sent_txts:
        print(sent_txt)


# Call each function
# Now use the copy of the original txts (txts[:]) list instead.
send_messages(txts[:], sent_txts)
show_messages(sent_txts)

# After calling the function, print both of your lists to show that
# the original list has retained its messages.
print("\n List of texts:")
print(txts)
print(sent_txts)

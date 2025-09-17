# Start with 8-7 album.py

# Write a make_album function() that builds a dictionary describing an album.
# Add an optional parameter for number of songs.
# Had num_of_songs at first but decided to go with tracks instead. To keep it simpler.

# A good chance to show off some ClariS albums!
def make_album(artist, album=None, tracks=0, ):
    """Building a dictionary that describes a music album."""
    album = {'Artist': artist,
             'Album': album,
             }
    if tracks:
        album['Tracks'] = tracks
    return album


# Make prompts for the inputs.
artist_prompt = "\nGive me an artist: "
album_prompt = "Give me one of their albums: "

# We are dealing with a while loop so give the user a way to stop.
print("Enter 'stop' if you wish to stop.")

while True:
    artist = input(artist_prompt)
    if artist == 'stop':
        break

    album_title = input(album_prompt)
    if album_title == 'stop':
        break

    album = make_album(artist, album_title)
    print(album)

print("\nSee ya!")
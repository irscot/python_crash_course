# Write a make_album function() that builds a dictionary describing an album.
# Add an optional parameter for number of songs.
# Had num_of_songs at first but decided to go with tracks instead. To keep it simpler.

# A good chance to show off some ClariS albums!

def make_album(artist, album, tracks=0):
    """Building a dictionary that describes a music album."""
    album = {'Artist': artist, 'Album': album}
    if tracks:
        album['Tracks'] = tracks
    return album


print(make_album('ClariS', 'Party Time', 13))

print(make_album('ClariS', 'Parfaitoune'))

print(make_album('ClariS', 'Alive'))

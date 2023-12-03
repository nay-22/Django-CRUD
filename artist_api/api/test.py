from models import Artist

# Retrieve all objects
all_artists = Artist.objects.all()

# Print the objects
for artist in all_artists:
    print(artist.name, artist.user.username, artist.works.all())

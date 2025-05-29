class Song:
    
    count = 0
    artists = []
    genres = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.artists.append(artist)
        Song.count += 1
        Song.genres.append(genre)

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_genres(cls):
        return list(set(cls.genres))

    @classmethod
    def get_artists(cls):
        return list(set(cls.artists))

    @classmethod
    def genre_count(cls):
        return {genre: cls.genres.count(genre) for genre in set(cls.genres)}

    @classmethod
    def artist_count(cls):
        return {artist: cls.artists.count(artist) for artist in set(cls.artists)}
    
     


test = Song("Lamba Lolo", "Ethic", "Gengetone")
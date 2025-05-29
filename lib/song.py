class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.artists.append(artist)
        Song.count += 1
        Song.genres.append(genre)

        # Update genre_count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist_count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_genres(cls):
        return list(set(cls.genres))

    @classmethod
    def get_artists(cls):
        return list(set(cls.artists))
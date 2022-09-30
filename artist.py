class Artist:
    def __init__(self, firstName, lastName, birtYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birtYear = birtYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birtYear

    def getAlbums(self):
        return self.__albums

    def getSingle(self):
        return self.__singles

    def mostLikedSong(self):
        empty = []
        for album in self.getAlbums():
            for song in album.getSongs():
                empty.append(song.getLikes())
        for singles in self.getSingle():
            empty.append(singles.getLikes())
        return empty[empty.index(max(empty))]

    def leastLikedSong(self):
        empty = []
        for album in self.getAlbums():
            for song in album.getSongs():
                empty.append(song.getLikes())
        for singles in self.getSingle():
            empty.append(singles.getLikes())
        return empty[empty.index(min(empty))]

    def totalLikes(self):
        empty = []
        total = 0
        for album in self.getAlbums():
            for song in album.getSongs():
                empty.append(song.getLikes())
        for singles in self.getSingle():
            empty.append(singles.getLikes())
        for i in range(len(empty)):
            total += empty[i]
        return total

    def topSongInAlbums(self):
        minInt = -9223372036854775807
        nameOfThatSong = ""
        allSongs = []

        for eachAlbum in self.__albums:
            for eachSong in eachAlbum.getSongs():
                allSongs.append(eachSong)

        for eachSong in allSongs:

            if minInt < eachSong.getLikes():
                minInt = eachSong.getLikes()
                nameOfThatSong = eachSong.getTitle()

        return [minInt, nameOfThatSong]

    def getTopSongFromSingles(self):
        minInt = -9223372036854775807
        topSongFromSingles = ""
        for eachSingle in self.__singles:

            if minInt < eachSingle.getLikes():
                topSongFromSingles = eachSingle.getTitle()
                minInt = eachSingle.getLikes()

        return [minInt, topSongFromSingles]

    def __str__(self):
        return f'Name:{self.__firstName} {self.__lastName},Birth Year:{self.__birtYear},Total Likes:{self.totalLikes()}'

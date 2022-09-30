class Album:

    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def addSongs(self, *songs):
        empty1 = []
        empty2 = []
        count = 0
        for song in songs:
            for i in self.__songs:
                empty1.append(i.getTitle())
                empty1.append(i.getReleaseYear())
                empty1.append(i.getDuration())
                empty2.append(empty1)
                empty1 = []
            if [song.getTitle(), song.getReleaseYear(), song.getDuration()] not in empty2:
                self.__songs.append(song)
                count += 1
        return count

    def sortBy(self, byKey, reverse):
        if reverse:
            return sorted(self.__songs, key=byKey)
        else:
            return sorted(self.__songs, key=byKey)[::-1]

    def sortByName(self, reverse):
        return self.sortBy(lambda x: x.getTitle(), reverse)

    def sortByPopularity(self, reverse):
        return self.sortBy(lambda x: x.getLikes(), reverse)

    def sortByDuration(self, reverse):
        return self.sortBy(lambda x: x.getDuration(), reverse)

    def sortByReleaseYear(self, reverse):
        return self.sortBy(lambda x: x.getReleaseYear(), reverse)

    def getTotalLikes(self):
        total = 0
        for song in self.__songs:
            total += song.getLikes()
        return total

    def __str__(self):
        songs = " "
        for song in self.__songs:
            songs += song.__str__() + "|"
        songs = songs[:len(songs) - 1]
        return f'Title:{self.__title},Release Year:{self.__releaseYear},Songs:{songs}'

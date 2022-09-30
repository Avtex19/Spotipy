class SpotiPy:

    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *artist):
        for eachArtist in artist:
            notEqualTo = 1
            for eachOne in self.__artists:
                if eachArtist.getFirstName() == eachOne.getFirstName() and \
                        eachArtist.getSecondName() == eachOne.getSecondName() and \
                        eachArtist.getBirthYear() == eachOne.getBirthYear():
                    notEqualTo -= 1
            if notEqualTo == 1:
                self.__artists.append(eachArtist)

    def getTopTrendingArtist(self):
        empty1 = []
        empty2 = []
        empty3 = []
        for artist in self.__artists:
            empty1.append(artist)
            empty1.append(artist.totalLikes())
            empty2.append(empty1)
            empty1 = []
        for i in self.__artists:
            empty3.append(i.totalLikes())
        if len(empty3) != 0:
            arr = empty2[empty3.index(max(empty3))]
            x = arr[0].getFirstName()
            y = arr[0].getSecondName()
            tpl = (x, y)
            return tpl

    def getTopTrendingAlbum(self):
        empty1 = []
        empty2 = []
        empty3 = []
        for artist in self.__artists:
            for album in artist.getAlbums():
                empty1.append(album)
                empty1.append(album.getTotalLikes())
                empty2.append(empty1)
                empty1 = []
            for i in artist.getAlbums():
                empty3.append(i.getTotalLikes())
        if len(empty3) != 0:
            arr = empty2[empty3.index(max(empty3))]
            return arr[0].getTitle()

    def getTopTrendingSong(self):
        topSongs = []
        for artist in self.__artists:
            topSongs.append(artist.topSongInAlbums())
            topSongs.append(artist.getTopSongFromSingles())

        minInt = -9223372036854775807
        topSong = ""
        for eachSong in topSongs:
            if minInt < eachSong[0]:
                minInt = eachSong[0]
                topSong = eachSong[1]

        return topSong

    def loadFromFile(addres):
        f = open('data/data3.txt', 'r')
        l = []
        index = 0
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        data = ''
        for i in lines:
            data += i
        data = data.replace(' ', '')
        # i make one string
        artistList = data.split("#")
        names = []
        albums = []
        for i in artistList:
            if i.__contains__('artists') or i.__contains__('Artists'):
                names.append(i[9:i.find('albums')])
                albums.append(i[i.find('albums') + 7::])
            else:
                names.append(i[:i.find('albums')])
                albums.append(i[i.find('albums') + 7::])
        splitedalbums = []

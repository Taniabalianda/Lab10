class Film:
    _numOfFilmsFinished = 0

    def __init__(self,

                 nameOfFilm="NoName", durationInMinutes=0, numberOfReviewsOnIMDB=0,
                 genre="NoGenre", releaseDate=0, director="NoDirector"

                 ):
        self._name = nameOfFilm
        self._durationInMinutes = durationInMinutes
        self._numberOfReviewsOnIMDB = numberOfReviewsOnIMDB
        self._genre = genre
        self._releaseDate = releaseDate
        self._director = director

    def __del__(self):
        print("I have deleted", self._name)
        print("I have deleted %s" % self._name)
        print(f"{self._name} was deleted")

    def __str__(self):
        return ', '.join((f"{name[1:]} = {capacity}" for name, capacity in self.__dict__.items()))

    __repr__ = __str__

    @staticmethod
    def finishedFilms(numberOfFinishedFilms):
        Film._numOfFilmsFinished += numberOfFinishedFilms


def main():
    harryPotter = Film("Harry Potter", 152, 564279, "fantasy", 4, "Chris Columbus")
    southpaw = Film("Southpaw")
    greenMile = Film("Green Mile", durationInMinutes=189)

    print(greenMile)
    print(southpaw)
    print(harryPotter)
    print(Film._numOfFilmsFinished)
    Film.finishedFilms(3)
    print(Film._numOfFilmsFinished)

if __name__ == '__main__':
    main()
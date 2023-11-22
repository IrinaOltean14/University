class Movie:
    def __init__(self, movie_id, title, description, genre):
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id):
        self._movie_id = movie_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def __str__(self):
        return f'{self.movie_id} -> {self.title}, {self.description}, {self.genre}'


def test_movie():
    movie = Movie('123', 'Iron Man', 'Marvel movie', 'Action')
    assert movie.movie_id == '123'
    assert movie.title == 'Iron Man'
    assert movie.description == 'Marvel movie'
    assert movie.genre == 'Action'

    movie.genre = 'Sci-Fi'
    assert movie.genre == 'Sci-Fi'

    assert str(movie) == '123 -> Iron Man, Marvel movie, Sci-Fi'


if __name__ == '__main__':
    test_movie()

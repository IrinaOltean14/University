from datetime import date, timedelta


class Rental:
    def __init__(self, rental_id, movie_id, client_id, rental_date, due_date, returned_date=None):
        self._rental_id = rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rental_date = rental_date
        self._due_date = due_date
        self._returned_date = returned_date

    @property
    def rental_id(self):
        return self._rental_id

    @rental_id.setter
    def rental_id(self, rental_id):
        self._rental_id = rental_id

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id):
        self._movie_id = movie_id

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def rental_date(self):
        return self._rental_date

    @rental_date.setter
    def rental_date(self, rental_date):
        self._rental_date = rental_date

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def returned_date(self):
        return self._returned_date

    @returned_date.setter
    def returned_date(self, returned_date):
        self._returned_date = returned_date

    def __str__(self):
        return f'{self._rental_id} -> movie id: {self._movie_id}, client id: {self._client_id}, rental date: {self._rental_date}, due date: {self._due_date}, returned date: {self._returned_date}'


def test_rental():
    d1 = date(2022, 12, 15)
    print(type(d1))
    d2 = d1 + timedelta(10)
    rental = Rental('1', '2', '3', d1, d2)
    assert rental.rental_id == '1'
    assert rental.movie_id == '2'
    assert rental.client_id == '3'
    assert rental.rental_date == d1
    assert rental.due_date == d2


if __name__ == '__main__':
    test_rental()

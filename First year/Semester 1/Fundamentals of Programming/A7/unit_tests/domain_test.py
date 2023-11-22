import unittest
from src.domain.movie import Movie
from src.domain.client import Client
from src.domain.rental import Rental
from datetime import date


class Test_Domain(unittest.TestCase):
    def test_movie1(self):
        movie = Movie('1', 'Batman', 'DC movie', 'Action')
        self.assertEqual(movie.movie_id, '1')
        self.assertEqual(movie.title, 'Batman')
        self.assertEqual(movie.description, 'DC movie')
        self.assertEqual(movie.genre, 'Action')

    def test_movie2(self):
        movie = Movie('1', 'Batman', 'DC movie', 'Action')
        movie.genre = 'Sci-Fi'
        self.assertEqual(movie.genre, 'Sci-Fi')

    def test_client1(self):
        client = Client('123', 'Andra Tresca')
        self.assertEqual(client.client_id, '123')
        self.assertEqual(client.name, 'Andra Tresca')

    def test_client2(self):
        client = Client('123', 'Andra Tresca')
        client.name = 'Maria Alexutan'
        self.assertEqual(client.name, 'Maria Alexutan')

    def test_rental1(self):
        rental_date = date(2022, 10, 10)
        due_date = date(2022, 11, 11)
        rental = Rental('1', '5', '10', rental_date, due_date)
        self.assertEqual(rental.rental_id, '1')
        self.assertEqual(rental.movie_id, '5')
        self.assertEqual(rental.client_id, '10')
        self.assertEqual(rental.rental_date, rental_date)
        self.assertEqual(rental.due_date, due_date)

    def teste_rental2(self):
        rental_date = date(2022, 10, 10)
        due_date = date(2022, 11, 11)
        rental = Rental('1', '5', '10', rental_date, due_date)
        rental.rental_id = '123'
        self.assertEqual(rental.rental_id, '123')


if __name__ == '__main__':
    Test_Domain()

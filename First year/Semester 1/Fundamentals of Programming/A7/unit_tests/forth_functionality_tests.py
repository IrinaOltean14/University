import unittest
from src.repository.repo import RentalRepo, MovieRepo, ClientRepo
from src.services.service import MovieService, ClientService, RentalService, Statistics
from src.domain.validators import MovieValidator, ClientValidator, RentalValidator
from datetime import date


class TestStatistics(unittest.TestCase):
    def setUp(self) -> None:
        self._rental_repo = RentalRepo()
        self._movie_repo = MovieRepo()
        self._client_repo = ClientRepo()
        self._movie_service = MovieService(self._movie_repo, MovieValidator())
        self._client_service = ClientService(self._client_repo, ClientValidator())
        self._rental_service = RentalService(self._rental_repo, RentalValidator(), self._movie_repo, self._client_service, self._movie_service, self._client_service)
        self._statistics = Statistics(self._rental_repo, self._movie_service, self._client_service, self._rental_service)

    def tearDown(self) -> None:
        pass

    def test_most_rented_movies_service(self):
        self._movie_service.add_movie_service('2','ceva', 'altceva', 'Comedy')
        self._movie_service.add_movie_service('4', 'ewf', 'efwe', 'Horror')
        self._client_service.add_client_service('1', 'Ana')
        self._client_service.add_client_service('3', 'Mihai')
        rental_date = date(2022, 1, 1)
        self._rental_service.rent_a_movie_service('1', '2', rental_date)
        rental_date = date(2022, 10, 12)
        self._rental_service.rent_a_movie_service('3', '4', rental_date)
        movie1 = self._movie_service.find_movie_by_id('2')
        movie2 = self._movie_service.find_movie_by_id('4')
        movie_list = []
        movie_list.append(movie1)
        movie_list.append(movie2)
        self.assertEqual(self._statistics.most_rented_movies_service(), movie_list)

    def test_most_active_clients(self):
        self._movie_service.add_movie_service('2', 'ceva', 'altceva', 'Comedy')
        self._movie_service.add_movie_service('4', 'ewf', 'efwe', 'Horror')
        self._client_service.add_client_service('1', 'Ana')
        self._client_service.add_client_service('3', 'Mihai')
        rental_date = date(2022, 1, 1)
        self._rental_service.rent_a_movie_service('1', '2', rental_date)
        rental_date = date(2022, 10, 12)
        self._rental_service.rent_a_movie_service('3', '4', rental_date)
        client1 = self._client_service.find_client_by_id('1')
        client2 = self._client_service.find_client_by_id('3')
        client_list = [client1, client2]
        self.assertEqual(self._statistics.most_active_clients_service(), client_list)

    def test_late_rentals_service(self):
        self._movie_service.add_movie_service('2', 'ceva', 'altceva', 'Comedy')
        self._movie_service.add_movie_service('4', 'ewf', 'efwe', 'Horror')
        self._client_service.add_client_service('1', 'Ana')
        self._client_service.add_client_service('3', 'Mihai')
        rental_date = date(2022, 1, 1)
        self._rental_service.rent_a_movie_service('1', '2', rental_date)
        rental_date = date(2022, 12, 18)
        self._rental_service.rent_a_movie_service('3', '4', rental_date)
        late_rental = self._rental_service.search_rental_by_rental_id('1')
        late_rental_list = [late_rental]
        self.assertEqual(self._statistics.late_rentals_service(), late_rental_list)
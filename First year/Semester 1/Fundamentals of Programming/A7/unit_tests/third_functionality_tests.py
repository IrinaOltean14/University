import unittest
from src.repository.repo import MovieRepo, ClientRepo
from src.domain.validators import MovieValidator, ClientValidator
from src.services.service import MovieService, ClientService


class TestThirdFunctionality(unittest.TestCase):
    def setUp(self) -> None:
        self._movie_service = MovieService(MovieRepo(), MovieValidator())
        self._client_service = ClientService(ClientRepo(), ClientValidator())

    def tearDown(self) -> None:
        pass

    def test_search_movie_service(self):
        self._movie_service.add_movie_service('1', 'Batman', 'DC movie', 'Action')
        self._movie_service.add_movie_service('2', 'Spiderman', 'Marvel movie', 'Action')
        self._movie_service.add_movie_service('3', 'Iron Man', 'Marvel movie', 'Action')
        movie1 = self._movie_service.find_movie_by_id('2')
        movie2 = self._movie_service.find_movie_by_id('3')
        movie_list = []
        movie_list.append(movie1)
        movie_list.append(movie2)
        self.assertEqual(self._movie_service.search_movie_service('marvel'), movie_list)
        self.assertEqual(self._movie_service.search_movie_service('comedy'), [])

    def test_search_client_service(self):
        self._client_service.add_client_service('1', 'Ana Maria')
        self._client_service.add_client_service('2', 'Ana Mierloi')
        self._client_service.add_client_service('3', 'Ion Pop')
        client1 = self._client_service.find_client_by_id('1')
        client2 = self._client_service.find_client_by_id('2')
        client_list = []
        client_list.append(client1)
        client_list.append(client2)
        self.assertEqual(self._client_service.search_client_service('ana'), client_list)
        self.assertEqual(self._client_service.search_client_service('Gabriel'), [])